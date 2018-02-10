#!/usr/bin/env python

from sys import argv
import string

import argparse

first, second, third = argv

def number_of_words(second, third):
    list1 = []
    list2 = []
    lower_list1 = []
    lower_list2 = []
    try:
        with open(second, 'r') as wap, open(third, 'r') as new:
                for line in wap:

                    words = line.strip().split()
                    list1.extend(words)

                for line1 in new:
                    words1 = line1.strip().split()
                    list2.extend(words1)
    #make letters lower case--------------
        for i in list1:
            lower1 = i.lower()
            lower_list1.append(lower1)
        for i in list2:
            lower = i.lower()
            lower_list2.append(lower)
    #Unique words---------------- by making set
        lower_list1 = [s.translate(None, string.punctuation) for s in lower_list1]
        lower_list1 = [s for s in lower_list1 if s]
        all_words_wap = set(lower_list1)


        lower_list2 = [s.translate(None, string.punctuation) for s in lower_list2]
        lower_list2 = [s for s in lower_list2 if s]
        all_words_wl = set(lower_list2)

    #printing-------------------------
        print second,":"
        print "\t", len(list1), "words"
        print "\tUnique:", len(all_words_wap)
        print third, ":"
        print "\t", len(list2), "words"
        print "\tUnique:", len(all_words_wl)

    #words only in one of them and words in both
        union_set = all_words_wap.union(all_words_wl)
        intersection_set = all_words_wap.intersection(all_words_wl)

        print "Only War and peace.txt:", len(union_set - all_words_wl)
        print "Only words.txt:", len(union_set - all_words_wap)
        print "Both files:", len(intersection_set)


    except IOError:
        print "Please enter valid existing file as 1st argument"


if __name__ == '__main__':

    number_of_words(second, third)