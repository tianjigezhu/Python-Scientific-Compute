#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:28:23 2017

@author: skycancer
"""

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])

print a
print b
print c

print a.shape
print b.shape
print c.shape

c.shape = 4, 3
print c

c.shape = 2, -1
print c
print c.shape

d = a.reshape((2, 2))
print a
print d

a[1] = 100
print a
print d

print c.dtype
print "\n"

ai32 = np.array([1, 2, 3, 4], dtype=np.int32)
af = np.array([1, 2, 3, 4], dtype=float)
ac = np.array([1, 2, 3, 4], dtype=complex)
print ai32
print ai32.dtype
print "\n"
print af
print af.dtype
print "\n"
print ac
print ac.dtype
print "\n"

# print numpy's type string
for key, value in np.typeDict.items():
    print key, " ", value
    
print "\n"

print set(np.typeDict.values())

a = np.int16(200)
#print a*a

v1 = 3.14
v2 = np.float64(v1)


t1 = np.array([1, 2, 3, 4], dtype=np.float)
t2 = np.array([1, 2, 3, 4], dtype = np.complex)
t3 = t1.astype(np.int32)
t4 = t2.astype(np.complex64)

print t1
print t2
print t3
print t4
print "\n"

print np.arange(0, 1, 0.1)
print np.linspace(0, 1, 10)
print np.linspace(0, 1, 10, endpoint=False)
print np.logspace(0, 2, 5)
print np.logspace(0, 2, 5, endpoint=False)
print np.logspace(0, 2, 4)
print np.logspace(0, 2, 10)
print "\n"
print np.logspace(0, 1, 12, base=2, endpoint=False)
"\n"
print np.empty((2, 3), np.int)
print np.zeros(4, np.int)
print np.ones(4, np.int)
print np.full(4, np.pi)
print np.full((2, 3), np.pi)
print "\n"

s = 'abcdefgh'
print np.fromstring(s, dtype = np.int8)
print "\n"

def func(i):
    return i % 4 + 1

print np.fromfunction(func, (10,))

def func2(i, j):
    return (i + 1) * (j + 1)
print np.fromfunction(func2, (9, 9))
print "\n"

a = np.arange(10)
print a
print a[5]
print a[3:5]
print a[:5]
print a[:-1]
print "\n"

a = np.arange(0, 100, 10).reshape(-1, 1)
print a
b = np.arange(0, 10)
print b
print a + b