#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 16:24:31 2018

@author: caseytaylor
"""

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
words = lorem_ipsum.split() # creates list of words from string 
word_counts = []
for i in words:
    # create list with word counts
    word_counts.append(words.count(i)) 
# zip two lists together- create a list of tuples 
zip(words,word_counts) 
lorem_dict = {word:count for word, count in zip(words,word_counts)}

print lorem_dict
print; print 


# calculate how many unique words are in lorem ipsum
# make a set 
lipsum_set = set(words)
# calculate unique words in the set
print len(lipsum_set) 
print; print

# more efficient method using counter
lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# create list of words from string
words = lorem_ipsum.split()  
# initialize empty dictionary
frequency = {} 
# loop through each word in word list
for i in words:  
    count = frequency.get(i,0) 
    frequency[i] = count + 1 
print frequency
print;print

f = open('agatha.txt', 'r')
# check for successful file open
# print f 



# efficient method
# f.read() reads and returns entire file as a string (with omitted size parameter)
agatha_words = (f.read()).split() # creates list of words from string 
frequency = {} # initialize empty dictionary
for i in agatha_words: # loop through each word in word list 
    # print i
    count = frequency.get(i,0) # dict.get(key, default = None), returns a value for the given key, otherwise returning 0 if key does not exist
    # print count
    frequency[i] = count + 1 
    # print frequency
print frequency
