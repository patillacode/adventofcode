#!/usr/bin/env python


def generate_new_number(string):
    # list of tuples such as (times a number appear, the number)
    results = []
    # If the number is one char long we return 1 times that number
    # (1, number)
    if len(string) == 1:
        return [(1, string)]
    # Another extreme case is when the given string is all the same
    # number repeated: 1111, 222, 33333 etc
    else:
        # Check if the number is all the same chars
        diff = False
        char = string[0]
        for i in string:
            if i != char:
                diff = True
                break
        # No different chars? return the length, easy :P
        if not diff:
            return [(len(string), char)]

    # If no extreem cases are found, the real thing comes to play
    # we read the string and for each char that is the same to one before
    # we increment the times of that char.
    # Managing the results might look a little messy but since is it a list
    # of tuples, I need to pop, create a new tuple and append it
    # (tuples cannot be modified)
    prev_char = ''
    for i in string:
        # Same char as before? increment times
        if i == prev_char:
            times = results[-1][0] + 1
            results.pop()
            results.append((times, i))
        # Not the same char as the one preceeding?
        # It might be time to create a tuple (restart the process)
        else:
            results.append((1, i))

        prev_char = i

    # return in string format
    # create a list of strings and join them in one string
    new_number_list = []
    # go through the list (each item is a tuple)
    for t in results:
        # go through the tuples
        for i in t:
            new_number_list.append(str(i))

    return ''.join(new_number_list)


input_string = '1113222113'
new_number = None

for i in range(50):
    if i == 0:
        new_number = generate_new_number(input_string)
    else:
        new_number = generate_new_number(new_number)

    # part 1 is 40 times
    if i == 39:
        print "Part 1: {0}".format(len(new_number))
# part 2 is 50 times
print "Part 2: {0}".format(len(new_number))
