#!/usr/bin/env python
import re


def pair_twice(string):
    pair_list = [''.join(pair) for pair in zip(string[:-1], string[1:])]
    for pair in pair_list:
        if len(re.findall(pair, string)) > 1:
            return True
    return False


def repeat_with_one_in_the_middle(string):
    # we will work in groups of three
    # first, middle, last(the actual letter)
    first = ''
    middle = ''
    for letter in string:
        if letter is first:
            return True
        first = middle
        middle = letter
    return False

nice_strings_counter = 0
input_text = open('input.txt')
for line in input_text:
    if pair_twice(line) and repeat_with_one_in_the_middle(line):
        nice_strings_counter += 1

print "Number of nice strings: {0}".format(nice_strings_counter)
