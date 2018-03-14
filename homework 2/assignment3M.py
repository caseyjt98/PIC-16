#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 19:54:32 2018

@author: caseytaylor
"""
import time 

def my_divide1(a,b):
    # list comprehension
    print [(float(ai)/bi) for ai,bi in zip(a,b)]
   

def my_divide2(a,b): 
    inputsValid = True
    for i in b:
        if i == 0 or isinstance(i,str):
            inputsValid = False
    for i in a:
        if isinstance(i,str):
            inputsValid = False
    if inputsValid:  
        print [(float(ai)/bi) for ai,bi in zip(a,b)]
    else: 
        return [], "Something's wrong with the inputs to my_divide2"  
    

def my_divide3(a,b):
    try:
        print [(float(ai)/bi) for ai,bi in zip(a,b)]
    except:
        return [], "Something's wrong with the inputs to my_divide3" 
    
    
    
start = time.clock()
a = range(0,1000000); b = range(1,1000001)
my_divide2(a,b) # 3.489 seconds
my_divide3(a,b) # 2.413 seconds
elapsed = (time.clock() - start)
print elapsed

print; print 


a = range(0,1000000); b = range(1,1000000)+ [0]
my_divide2(a,b)
my_divide3(a,b)
print;print


a = range(0,1000000); b = range(1,1000000)+ ['a']
my_divide2(a,b)
my_divide3(a,b)
print;print



def my_divide4(a,b):
    try:
        [(float(ai)/bi) for ai,bi in zip(a,b)]
    except ZeroDivisionError:
        print "There is a zero in b"
    except TypeError:
        print "Non-numeric data detected"
    except ValueError:
        print "Non-numeric data detected"

