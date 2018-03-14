#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 16:53:02 2018

@author: caseytaylor
"""
from __future__ import division
import urllib
import nltk

""" Step 2 """
url = 'http://www.gutenberg.org/files/863/863-0.txt'
response = urllib.urlopen(url)
raw = response.read().decode('utf8')
# print type(raw) # unicode
# print len(raw) # variable raw contains unicode with 349458 characters
raw[:85]


""" Step 3 """
starting_index = raw.rfind("CHAPTER I. I GO TO STYLES") 
print starting_index

print raw.rfind("THE END") 
ending_index = 330282 + 7
print ending_index
text = raw[starting_index:ending_index]
print len(text) # length of updated text
print text[0:330289] # check
# print type(text)

""" Step 4 """
# from assignment 2W...
words = text.split() # create list of words from string
frequency = {} 
for i in words:  
    count = frequency.get(i,0) 
    frequency[i] = count + 1 
# print frequency


fdist = nltk.FreqDist(words)
print fdist
# print fdist['want'] # check
# print fdist['wing'] # check
print fdist.most_common(20)

# check for  same result
print fdist ['the']
print frequency['the']
print len(fdist)
print len(words)

lexical_diversity = len(fdist) / len(text)
print lexical_diversity


""" Step 5 """
new_text = text.replace('_','') # eliminate underscores
print new_text[:500]  # check

tokens = nltk.word_tokenize(new_text) # create list of words/ punctuation 
# print tokens[:100]

new_fdist = nltk.FreqDist(tokens)
print new_fdist
# print new_fdist.most_common(20)

new_lexical_diversity = len(new_fdist) / len(new_text)
print new_lexical_diversity


""" Step 6 """
# make all text lowercase
lowercase_text = new_text.lower()
# print lowercase_text

lowercase_tokens = nltk.word_tokenize(lowercase_text)

caseInsensitive_fdist = nltk.FreqDist(lowercase_tokens)
print caseInsensitive_fdist
print caseInsensitive_fdist.most_common(20)


""" Step 7 """
porter = nltk.PorterStemmer()
stems = [porter.stem(t) for t in lowercase_tokens]
# print stems[:100]

stem_fdist = nltk.FreqDist(stems)
print stem_fdist


""" Step 8 """
textObject = nltk.Text(tokens)
type(textObject)
print textObject[0:50]

textObject.concordance("point")


""" Step 9 """
# optional


""" Step 10 """
print new_fdist.most_common(50)


""" Step 11 """
print caseInsensitive_fdist
myList = caseInsensitive_fdist.most_common(6158)

freqList = []

for x in myList:
     if x[0][0] < 'z' and x[0][0] > 'a':
            freqList.append(x)
print freqList