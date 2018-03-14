#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:00:59 2018

@author: caseytaylor
"""

import csv
import re 

# get list of names in format 'first last'
with open('data.csv', 'r') as F:
    csv_reader = csv.reader(F)
    next(csv_reader)
    
    names = []
    for row in csv_reader:
        # match format 'last, first'
        # regex captures (first) (last)
        pattern = r'(\w+),\s?(\w+)'
        # change format to 'first last'
        full_name = re.sub(pattern, r'\2 \1', row[0])
        names.append(full_name)
        
    
    
# get list of phone numbers with zip codes and all dashes (no dots)
with open('data.csv', 'r') as F:
    csv_reader = csv.reader(F)
    next(csv_reader) # skip header
    
    all_numbers = []
    Phone = []
    for row in csv_reader:
        number = row[1].replace('.','-') # replace dots with dashes
        all_numbers.append(number) # append to list all_numbers
        pattern = re.compile(r'\(?\d{3}\)?\s?[\.-]?\d{3}\.?-?\d{4}$')
        # create new list including only zip code #s
        Phone = filter(pattern.match, all_numbers)
        
        
    
# get list of phone numbers with zip codes and all dashes (no dots)

pattern = re.compile(r'1?\-?\(?\d{3}\)?\s?[\.-]?\d{3}\.?-?\d{4}$') # pattern to match

with open('data.csv','r') as F: # open file
    
    csv_reader = csv.reader(F)
    next(csv_reader) # skip header
    
    data2 = []
    
    for i in csv_reader:
        i[1] = i[1].replace('.','-') # replace dots with dashes
        if pattern.match(i[1]):
            data2.append(i)
            
data_new = []

for i in range(len(data2)): # iterate over rows 
    # match format 'last, first'
    # regex captures (first) (last)
    pattern = r'(\w+),\s?(\w+)'
    # change format to 'first last'
    full_name = re.sub(pattern, r'\2 \1', data2[i][0]) # replace pattern by switching capture groups
    data_new.append( [full_name, data2[i][1]] ) # this is an array!! [name, phone number]

# now get list of just names and just phone numbers!!!!
names = [item[0] for item in data_new]
numbers = [item[1] for item in data_new]


numbers2 = []
for i in range(len(numbers)): # iterate over list of numbers 
    # match format 318-266-1334
    pattern = r'(\d+)-(\d+-\d+$)'
    # change format to (318) 266-1334
    
    number = re.sub(pattern, r'(\1) \2', numbers[i]) # replace pattern
    numbers2.append(number) 



numbers3 = []
for i in range(len(numbers)): # iterate over list of numbers 
 # match format 3182661334
    pattern = r'1?(\d{3})(\d{3})(\d{4})'
    # change format to (318) 266-1334
    number = re.sub(pattern, r'(\1) \2-\3', numbers2[i]) # replace pattern
    numbers3.append(number) 


numbers4 = []
for i in range(len(numbers3)): # iterate over list of numbers 
 # match format 1-106-494-3219
    pattern = r'1-(\d{3})-(\d{3}-\d{4})$'
    # change format to (106) 494-3219
    number = re.sub(pattern, r'(\1) \2', numbers3[i]) # replace pattern
    numbers4.append(number) 


numbers5 = []
for i in range(len(numbers4)): # iterate over list of numbers 
 # match format 1-(540) 856-6725
    pattern = r'1-(\(\d{3}\)\s\d{3}-\d{4})$'
    # change format to (540) 856-6725
    number = re.sub(pattern, r'\1', numbers4[i]) # replace pattern
    numbers5.append(number) 
   
    
    
    
# NAMES

names2 = []
for i in range(len(names)): # iterate over list of numbers 
    # match format Candace Luna X.
    pattern = r'(\w+)\s(\w\.)$'
    # change format to Candace X. Luna
    name = re.sub(pattern, r'\2 \1', names[i]) # replace pattern
    names2.append(name) 


# separate FIRST, MI, LAST 

# get list of FIRST NAMES
first = []
pattern = re.compile(r'^(\w+)') # pattern to match for last name
  
for i in names2:
    result = pattern.findall(i)
    first.append(result[0])
# print len(first)


# get list of MI 
MI = []
pattern = re.compile(r'(\w\.)') # how to get middle intial if not everyone has middle initial??
for i in names2:
    if pattern.search(i):
        result = pattern.findall(i)
        MI.append(result[0])
        
    else:
        MI.append('') # leave blank spot
# print len(MI)


# get list of LAST NAMES
last = []
pattern = re.compile(r'(\w+$)') # pattern to match for last name
  
for i in names2:
    result = pattern.findall(i)
    last.append(result[0])
# print len(last)


rows = zip(first,MI,last,numbers5)

# open new file for writing
with open('data2.csv','w') as f:
    # create csv writer object, pass in new file to writer method
    csv_writer = csv.writer(f)
    csv_writer.writerow(["First", "M.I.","Last","Number"])
    for row in rows:
        csv_writer.writerow(row)