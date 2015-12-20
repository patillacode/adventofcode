#!/usr/bin/env python
# import itertools
# import sys

input_text = open('test.txt')

MAX_TEASPOONS = 100


def get_number_of_properties(ingredients):
    # ings = ingredients.copy()
    # return len(ings.popitem()[1])
    return len(ingredients.keys())


def create_ingredients():
    ingredients = {}

    for line in input_text:
        ingredient = line.split(':')[0]

        capacity = int(
            line.split('capacity ')[1].split(',')[0].replace('\n', ''))

        durability = int(
            line.split('durability ')[1].split(',')[0].replace('\n', ''))

        flavor = int(line.split('flavor ')[1].split(',')[0].replace('\n', ''))

        texture = int(
            line.split('texture ')[1].split(',')[0].replace('\n', ''))

        calories = int(
            line.split('calories ')[1].split(',')[0].replace('\n', ''))

        ingredients[ingredient] = {'capacity': capacity,
                                   'durability': durability,
                                   'flavor': flavor,
                                   'texture': texture,
                                   'calories': calories}
    return ingredients


def create_combinations(number_of_items, total_units):
    if number_of_items == 1:
        start = total_units
    else:
        start = 0
    combinations = []
    for i in range(start, total_units + 1):
        if number_of_items - 1:
            for t in create_combinations(number_of_items - 1, total_units - i):
                combinations.append([i] + t)
        else:
            combinations.append([i])
    return combinations


def calculate_recipes_score(ingredients, combinations):
    pass


if __name__ == '__main__':
    ingredients = create_ingredients()
    for k, v in ingredients.iteritems():
        print k, v
    print "#" * 30
    # sys.exit()
    combinations = create_combinations(
        get_number_of_properties(ingredients), MAX_TEASPOONS)
    print combinations
    scores = calculate_recipes_score(ingredients, combinations)
    print max(scores)
