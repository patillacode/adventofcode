#!/usr/bin/env python

input_text = open('input.txt')
total = 0
for line in input_text:
    # line[:-1] for the \n at the end of file
    # eval gives back the raw content of the string
    total += len(line[:-1]) - len(eval(line))
print total
