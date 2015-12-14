#!/usr/bin/env python

north = "^"
east = ">"
west = "<"
south = "v"

# start point
santa_current_pos = (0, 0)
robot_current_pos = (0, 0)

santa_houses_visited = set()
robot_houses_visited = set()

santa_houses_visited.add(santa_current_pos)
robot_houses_visited.add(robot_current_pos)

input_text = open('input.txt').read()
# switch between santa and robot
# odd = True (Santa)
# odd = False (Robot)
odd = True

for direction in input_text:

    if odd:
        current_pos = santa_current_pos
    else:
        current_pos = robot_current_pos

    if direction is north:
        current_pos = (current_pos[0], current_pos[1] + 1)
    elif direction is east:
        current_pos = (current_pos[0] + 1, current_pos[1])
    elif direction is west:
        current_pos = (current_pos[0] - 1, current_pos[1])
    elif direction is south:
        current_pos = (current_pos[0], current_pos[1] - 1)

    if odd:
        santa_houses_visited.add(current_pos)
        santa_current_pos = current_pos
        # Change turn
        odd = False
    else:
        robot_houses_visited.add(current_pos)
        robot_current_pos = current_pos
        # Change turn
        odd = True

# Union between both sets will give us all visited houses
houses_visited = santa_houses_visited.union(robot_houses_visited)
print "Santa and Robot Santa have visited at least once: {0} houses".format(
    len(houses_visited))
