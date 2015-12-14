#!/usr/bin/env python

north = "^"
east = ">"
west = "<"
south = "v"

# start point
current_pos = (0, 0)
houses_visited = set()
houses_visited.add(current_pos)

input_text = open('input.txt').read()
for direction in input_text:
    if direction is north:
        current_pos = (current_pos[0], current_pos[1] + 1)
    elif direction is east:
        current_pos = (current_pos[0] + 1, current_pos[1])
    elif direction is west:
        current_pos = (current_pos[0] - 1, current_pos[1])
    elif direction is south:
        current_pos = (current_pos[0], current_pos[1] - 1)

    # Only write down if the house is new since
    # we only care if santa has visited at least once
    # no duplicates :)
    if current_pos not in houses_visited:
        houses_visited.add(current_pos)

print "Santa has visited at least once: {0} houses".format(len(houses_visited))
