#!/usr/bin/env python
import re

input_text = open('input.txt').read()


def calculate_sum(string):
    # this grabs ALL numbers
    p = re.compile('\d+')
    positive_numbers = p.findall(string)

    # this grabs ALL negative numbers
    p = re.compile('-\d+')
    negative_numbers = p.findall(string)

    # remove all negative numbers from "all the numbers" list
    # to have two 'real' lists (positive_numbers and negative_numbers)
    for n in negative_numbers:
        s = str(abs(int(n)))
        positive_numbers.pop(positive_numbers.index(s))

    # sum of positive
    total_pos = 0
    for n in positive_numbers:
        total_pos += int(n)

    # sum of negative
    total_neg = 0
    for n in negative_numbers:
        total_neg += int(n)

    return total_pos + total_neg

if __name__ == '__main__':
    print "Total: {0}".format(calculate_sum(input_text))
