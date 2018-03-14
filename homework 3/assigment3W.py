#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:36:17 2018

@author: caseytaylor
"""

class MathVector:
    """MathVector class represents N-dimensional mathematical vectors"""  
    def __init__(self, *args):
        self.vec = []
        # if only one argument parameter
        if len(args) == 1: 
            # if arg parameter is single integer value
            if isinstance(args[0],int):
                components = args[0] 
                for i in range(components):
                    self.vec.append(0)

            # if arg parameter is a list
            if isinstance(args[0],list): 
                # loop through list 
                for i in args[0]: 
                    # append values
                    self.vec.append(i)   
                    
        # else if multiple argument parameters
        else: 
            # loop through parameters
            for i in args:
                # append values
                self.vec.append(i)

    def get_el (self,index):
        """returns the i-th component of the vector"""
        try:
            return self.vec[index-1]
        except IndexError:
            print "list index out of range."
            
    def neg(self):
        negVec = [(-i) for i in self.vec]
        return MathVector(negVec)
        
    def mag(self):
        squareVec = [i**2 for i in self.vec]
        sumSquares = 0
        for i in squareVec:
            sumSquares = sumSquares + i 
        return (sumSquares**0.5)
    
    def dot(self, vec2):
        return sum(x*y for x,y in zip(self.vec, vec2.vec))
    
    def plus(self, vec2):
        return MathVector([x+y for x,y in zip(self.vec, vec2.vec)])
        
        
    def sp(self, scalar):
        return MathVector([x*scalar for x in self.vec])
    
    def print_me(self):
        print self.vec
        
    def __getitem__(self,key):
        return self.vec[key-1]
    
    def __neg__(self):
        return self.neg()
    
    def __abs__(self):
        return self.mag()
        
    def __add__(self, vec2):
        return self.plus(vec2)
    
    def __mul__(self,arg): 
        # if arg is a scalar
        if isinstance(arg, int):
            return self.sp(arg) 
        else:
            return self.dot(arg)
        
    def __rmul__(self, scalar): 
        return self * scalar # reverses order of multiplication
    
    def __str__ (self):
        return str(self.vec)
    
    
        
u = MathVector(5)
print "u =",
u.print_me()
 
v = MathVector([2,3,6])
print "v =",
v.print_me()
 
w = MathVector(1,2,3)
print "w =",
w.print_me()
 
print v.get_el(2)
v.neg().print_me()
print v.mag()
print v.dot(w)
v.plus(w).print_me()
v.sp(3).print_me()
 
print v
print v[2]
print -v
print abs(v)
print v*w
print v+w
print v*3
print 3*v