#!/usr/bin/env python


def naive_next(string):
    stop = False
    list_string = list(string)

    index = -1
    while not stop:
        # get char
        current = list_string[index]
        # Check the Z condition
        if current == 'z':
            list_string[index] = 'a'
            index -= 1
            stop = False
        # Increment the letter
        else:
            list_string[index] = chr(ord(current) + 1)
            stop = True
    return ''.join(list_string)


def check_length(string):
    return True if len(string) == 8 else False


# Check method for requirement:
# Passwords must include one increasing straight of at least three letters
def check_straight(string):
    prev = '1'
    middle = '2'
    for letter in string:
        if ord(letter) == ord(middle) + 1 == ord(prev) + 2:
            return True
        prev = middle
        middle = letter
    return False


# Check method for requirement:
# May not contain the letters i, o, or l
def check_banned_chars(string):
    return False if 'i' in string or 'o' in string or 'l' in string else True


# Check method for requirement:
# Must contain at least two different, non-overlapping pairs of letters
def check_overlapping(string):
    counter = 0
    prev = ''
    middle = ''
    for letter in string:
        if letter == middle and letter != prev:
            counter += 1
        prev = middle
        middle = letter
    return True if counter > 1 else False


def next_password(password):
    valid = False
    while not valid:
        password = naive_next(password)
        if check_length(password) and \
           check_banned_chars(password) and\
           check_overlapping(password) and\
           check_straight(password):
                valid = True
    return password

input_string = 'hxbxwxba'
part_one_password = next_password(input_string)
print "Part 1 password is: {0}".format(part_one_password)
print "Part 2 password is: {0}".format(next_password(part_one_password))
