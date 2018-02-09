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
        print "name of book\n", second
        print "number of words:\n", num_words

    with open(third, 'r') as new:
        for line in new:
            words = line.split()
            num_words = num_words + len(words)
        print "name of book\n", third
        print "number of words:\n", num_words

def unique_words(second, third):
    with open(second, 'r') as wap:
        words = wap.read()
        word_list = words.split()
        all_words = set(word_list)
        print "wap\n", len(all_words)

    with open(third, 'r') as wl:
        words1 = wl.read()
        word_list1 = words1.split()
        all_words1 = set(word_list1)
        print "wl\n", len(all_words1)

def final_words(second, third):
    with open(second, 'r') as wap:
        words = wap.read()
        word_list = words.split()
        all_words_wap = set(word_list)

    with open(third, 'r') as wl:
        words1 = wl.read()
        word_list1 = words1.split()
        all_words_wl = set(word_list1)

    union_set = all_words_wap.union(all_words_wl)
    intersection_set = all_words_wap.intersection(all_words_wl)

    print "Only in war and peace:", len(union_set - all_words_wl) #aub - p(wl)
    print "Only in words:", len(union_set - all_words_wap) #aub - p(wap)
    print "Common in both", len(intersection_set)

if __name__ == '__main__':

    number_of_words(second, third)
    unique_words(second, third)
    final_words(second, third)