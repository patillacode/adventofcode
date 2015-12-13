#!/usr/bin/env python
from part1 import calculate_sum

input_text = open('input.txt').read()
blocks = eval(input_text)


def min_block(block):
    # if block is a number or a string, return that value
    if isinstance(block, str) or isinstance(block, int):
        return block
    # if block is a dict, ignore or process
    elif isinstance(block, dict):
        # ONLY RED IN THE VALUES!
        # Read carefully the instructions
        # ignore if red in its values
        if 'red' in block.values():
            return None
        # process otherwise
        else:
            ret = []
            for k, v in block.iteritems():
                ret.append(min_block(k))
                ret.append(min_block(v))
            return ret
    # if block is a list process
    elif isinstance(block, list):
        ret = []
        for item in block:
            ret.append(min_block(item))
        return ret

min_blocks = min_block([blocks])
print "Total: {0}".format(calculate_sum(str(min_blocks)))
