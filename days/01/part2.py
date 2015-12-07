#!/usr/bin/env python

import sys

plus = "("
minus = ")"
floor = 0
position = 0

input_text = open('instructions.txt').read()

for sign in input_text:
    position += 1
    if sign is plus:
        floor += 1
    elif sign is minus:
        floor -= 1

    if floor is -1:
        print "Position: {0}".format(position)
        sys.exit(2)
