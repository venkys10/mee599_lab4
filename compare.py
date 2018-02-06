#!/usr/bin/env python

from sys import argv

import argparse
'''
first, second, third = argv

print "first:", first
print "second:", second
print "third:", third
'''
def number_of_words(second, third):
    first, second = argv
    num_words = 0
    with open(second, 'r') as wap:
        for line in wap:
            words = line.split()
            num_words = num_words + len(words)

        print "number of words:", num_words

if '__name__'==
#test_words('foo', 'bar')
