#!/usr/bin/env python

plus = "("
minus = ")"
result = 0
input_text = open('instructions.txt').read()

for sign in input_text:
    if sign is plus:
        result += 1
    elif sign is minus:
        result -= 1

print "Result: {0}".format(result)
