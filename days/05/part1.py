#!/usr/bin/env python


def has_three_vowels(string):
    counter = 0
    for letter in string:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            counter += 1
            if counter is 3:
                return True
    return False


def has_double_letter(string):
    prev_letter = ''
    for i in string:
        if i is prev_letter:
            return True
        else:
            prev_letter = i
    return False


def has_custom_pair(string):
    custom_pairs = ['ab', 'cd', 'pq', 'xy']
    for pair in custom_pairs:
        if string.find(pair) is not -1:
            return True
    return False


nice_strings_counter = 0
input_text = open('input.txt')
for line in input_text:
    if has_three_vowels(line) and \
       has_double_letter(line) and \
       not has_custom_pair(line):

        nice_strings_counter += 1

print "Number of nice strings: {0}".format(nice_strings_counter)
