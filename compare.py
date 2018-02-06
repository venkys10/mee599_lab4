#!/usr/bin/env python

from sys import argv

import argparse

first, second, third = argv
def number_of_words(second, third):
    num_words = 0
    with open(second, 'r') as wap:
        for line in wap:
            words = line.split()
            num_words = num_words + len(words)
        print "name of book", second
        print "number of words:", num_words

    with open(third, 'r') as new:
        for line in new:
            words = line.split()
            num_words = num_words + len(words)
        print "name of book", third
        print "number of words:", num_words

if __name__ == '__main__':

    number_of_words(second, third)
#test_words('foo', 'bar')
