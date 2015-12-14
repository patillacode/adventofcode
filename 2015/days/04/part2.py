#!/usr/bin/env python

import hashlib


key = 'ckczppom'
keep_going = True
number = -1
while keep_going:
    number += 1
    md5_hash = hashlib.md5('{0}{1}'.format(key, number)).hexdigest()
    if md5_hash.startswith('000000'):
        keep_going = False

print 'Number: {0}'.format(number)
