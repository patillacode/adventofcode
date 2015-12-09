#!/usr/bin/env python

import itertools


# Create all (no repeat) permutations
# and return them like city->city->city->city
# for later parsing
def create_permutations(items_list):
    permutations = list()
    all_permutations = itertools.permutations(items_list)
    for p in list(all_permutations):
        new_perm = "->".join(p)
        if new_perm not in permutations:
            permutations.append(new_perm)
    return permutations


routes = {}
cities_list = []

input_text = open('input.txt')
for line in input_text:
    # Get all cities
    cities = line.split(' = ')[0].split(' to ')
    for c in cities:
        cities_list.append(c)

    # Get all routes
    origin = cities[0]
    destination = cities[1]
    distance = int(line.split(' = ')[1])
    if origin in routes:
        routes[origin].update({destination: distance})
    else:
        routes[origin] = {destination: distance}
input_text.close()

cities_list = set(cities_list)

# Create all permutations for cities given
perms = create_permutations(cities_list)


def get_distance(origin, destination):
    if origin in routes:
        if destination in routes[origin]:
            return routes[origin][destination]
        else:
            if origin in routes[destination]:
                return routes[destination][origin]
    elif destination in routes:
        if origin in routes[destination]:
            return routes[destination][origin]
    else:
        return False

# go through all perms and calculate the value of that route
# and store all route distances in a list
distances = []
for route in perms:
    cities = route.split('->')
    distance = 0
    for i in range(len(cities) - 1):
        distance += get_distance(cities[i], cities[i + 1])
    distances.append(distance)

# Select the min distance of the list
print "Part 1: Shortest distance is {0}".format(min(distances))
print "Part 2: Longest distance is {0}".format(max(distances))
