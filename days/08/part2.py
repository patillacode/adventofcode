#!/usr/bin/env python

input_text = open('input.txt')
total = 0
for line in input_text:
    # the difference between the newly encoded string "\"aaa\\\"aaa\""
    # and the original string literal                   "aaa \ "aaa "
    # is the added \\ and the added ""                "\    \ \    \ "
    # if we count the \s and "s in the original string and the \s and "s in the
    # new string the difference is always the number in the original + 2
    # Another example:
    # "\x27" becomes "\"\\x27\"" --> "\  \  \" --> 5 = 3(in the original) + 2
    total += line.count('\\') + line.count('"') + 2
print total
