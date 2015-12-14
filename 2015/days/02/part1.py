#!/usr/bin/env python


def get_total_area(l, w, h):
    area = (2 * l * w) + (2 * w * h) + (2 * h * l)
    extra_area = get_extra_area(l, w, h)
    return area + extra_area


def get_extra_area(l, w, h):
    dimensions = [l, w, h]
    # get pos of max value
    max_pos = dimensions.index(max(dimensions))
    # get max value out
    dimensions.pop(max_pos)

    return dimensions[0] * dimensions[1]


input_text = open('input.txt')
total_paper_area = 0
for line in input_text:
    dimensions = line.split('x')
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    total_paper_area += get_total_area(l, w, h)

print "{0} units of paper are needed".format(total_paper_area)

input_text.close()
