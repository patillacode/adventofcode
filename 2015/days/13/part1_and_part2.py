#!/usr/bin/env python
import itertools
# import sys
input_text = open('input.txt')


# Create object with all data from insatructions
def create_dinner_table():
    dinner_table = {}
    # parse instructions
    for line in input_text:
        name = line.split(' would gain ')[0].split()[0]
        action = line.split(' would ')[1].split()[0]
        value = line.split(' {0} '.format(action))[1].split()[0]
        next_to = line.split('next to ')[1].replace('.\n', '')
        if name not in dinner_table:
            dinner_table[name] = {}

        if action == 'lose':
            dinner_table[name].update({next_to: int(value) * -1})
        else:
            dinner_table[name].update({next_to: int(value)})
    return dinner_table


# Create all (no repeat) permutations
# and return them like name->name->name->name
# for later parsing
def create_permutations(items_list):
    permutations = list()
    all_permutations = itertools.permutations(items_list)
    for p in list(all_permutations):
        new_perm = "->".join(p)
        if new_perm not in permutations:
            permutations.append(new_perm)
    return permutations


# create all possible arrangements (based on permutations)
# with the happiness value each one has
def arrangements_by_happiness(permutations):
    arrangements = {}
    for p in permutations:
        names = p.split('->')
        happiness = []
        for n in names:
            index = names.index(n)
            prev_index = index - 1
            next_index = index + 1
            # limit cases
            if index == len(names) - 1:
                next_index = 0
            if index == 0:
                prev_index = len(names) - 1

            happiness.append(dinner_table[n][names[next_index]])
            happiness.append(dinner_table[n][names[prev_index]])
        arrangements[p] = sum(happiness)
    return arrangements

if __name__ == '__main__':
    # part 1
    dinner_table = create_dinner_table()
    permutations = create_permutations(dinner_table.keys())
    arrangements = arrangements_by_happiness(permutations)
    part1 = max(arrangements.values())

    # part 2
    # add myself to the dinner table
    dinner_table['myself'] = {}
    for name in dinner_table.keys():
        if name != 'myself':
            dinner_table[name].update({'myself': 0})
            dinner_table['myself'].update({name: 0})
    permutations = create_permutations(dinner_table.keys())
    arrangements = arrangements_by_happiness(permutations)
    part2 = max(arrangements.values())

    print "Maximum happiness value (part 1): {0}".format(part1)
    print "Maximum happiness value (part 2): {0}".format(part2)
