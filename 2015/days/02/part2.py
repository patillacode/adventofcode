#!/usr/bin/env python


def get_smallest_perimeter(l, w, h):
    dimensions = [l, w, h]
    # get pos of max value
    max_pos = dimensions.index(max(dimensions))
    # get max value out
    dimensions.pop(max_pos)

    return (dimensions[0] + dimensions[1]) * 2


def get_cubic_units(l, w, h):
    return l * w * h


def get_total_ribbon(l, w, h):
    return get_smallest_perimeter(l, w, h) + get_cubic_units(l, w, h)


input_text = open('input.txt')
total_ribbon = 0

for line in input_text:
    dimensions = line.split('x')
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    total_ribbon += get_total_ribbon(l, w, h)

print "{0} units of ribbon are needed".format(total_ribbon)

input_text.close()
