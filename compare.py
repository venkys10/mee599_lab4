#!/usr/bin/env python

from sys import argv

import argparse

first, second, third = argv
def number_of_words(second, third):
    num_words = 0

    with open(second, 'r') as wap:
        list1 = []
        for line in wap:
            words = line.split()
            num_words = num_words + len(words)
            list1.extend(words)
        all_words_wap = set(list1)
        all_words_wap = set(all_words_wap)
        print second,":"
        print "\t", num_words, "words"
        print "\tUnique:", len(all_words_wap)

    with open(third, 'r') as new:
        list2 = []
        for line in new:
            words = line.split()
            num_words = num_words + len(words)
            list2.extend(words)
        all_words_wl = set(list2)
        print third,":"
        print "\t", num_words, "words"
        print "\tUnique:", len(all_words_wl)

        union_set = all_words_wap.union(all_words_wl)
        intersection_set = all_words_wap.intersection(all_words_wl)

        print "Only war_and_peace.txt:", len(union_set - all_words_wap)
        print "Only words.txt:", len(union_set - all_words_wl)
        print "Both files:", len(intersection_set)
'''
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
'''
if __name__ == '__main__':

    number_of_words(second, third)
