# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 08:33:31 2017

@author: Jeffrey
"""
"""
1. Linear Search
"""
def linearSearch (F, target):
    for x in range(len(F)):
        if (F[x]==target):
            return x
    return False

"""
2. Exhaustive Enumeration
"""
from math import sqrt
def linearSearch_sqrt(N):
    epsilon = 0.001
    x = 0.000
    while x*x < N - epsilon:
        x += epsilon
    return x

print linearSearch_sqrt(15)
print sqrt(15)

"""
3. Binary Search
"""
def binarySearch(F, target):
    low = 0
    high = len(F) - 1
    idx = False
    
    while low <= high and not idx:
        mid = low + (high - low) / 2
        print "LOW {} Hi {} MID {}, comparing {} to {}".format(low, high, mid, target, F[mid])
        if F[mid] == target:
            return mid
        if F[mid] > target:
            high = mid -1
        else:
            low = mid + 1
    return False

F = range(32)
target = 4 
print "Looking for [{}] in array {}".format(target, F)
print binarySearch(F, target)

"""
 4. Bisection Search

monotonic functions are either entirely non-increasing or non-decreasing
output is like a sorted list, nondecreasing as x increases
"""

"""
5. Finding a square root
""" 
print 
print "This is the first problem assigned"
print "We will find the square root of 1000 as an example"
def bisection_search_kth_root(N,k):
    epsilon = 0.001
    low = 0.000
    high = 1000000.000
    x = 1.000
    count = 0 #keep track of the number of times the program loops through
    while abs((x**k) - N) > epsilon:    
        x = float(low + (high - low) / 2.0)
        print x
        count += 1
        print count, "loop(s)"
        if float(abs(x**k - N)) <= epsilon:
            return x
        if x**float(k) > N + epsilon:
            high = x
        else:
            low = x
#    return False

print bisection_search_kth_root(1000,2)
    
"""
6. Bounding N!
Notes
lg(N!) = sum lg i, i = 1, N
approx = integral of lg x dx, from i = 1 to N
which equals
    n*lg n - n + 1
        complexity = O(n lg n)
"""

"""
#7. Argmax constraint
"""
print
print "We will now determine the maximum factorial"
print"that can be stored in 2**43 bits (1Tb):"
from math import log
def bisection_search_lgN(N):
    epsilon = 0.001
    low = 0.000
    high = 0.001
    x = 1.0
    while high * log(high, 2) - high + 1 < 2**43:
        high = high * 2
    while low <= high:
        x = low + (high - low) / 2.0
        if abs(x * log(x,2) - x + 1 - 2**43) < epsilon:
            return x
        if x * log(x,2) - x + 1 > 2**43 - epsilon:
            high = x
        else:
            low = x
    return False

print bisection_search_lgN(2**43)
            

"""
8. Newton-Raphson

Used to find real-valued roots of different functions
finding x such that f(x) = 0
iterative method
    improve each guess of a root by
    y - (f(y))/(f'(y))
"""
print
print "Now here's the Newton method for sqrt 1000"
#example code for x**2 - k
#find sqrt(k)
def newton_sqrt(k):
    epsilon = 0.001
    y = k / 2.0 #guess
    count = 0 #keep track of loops
    while abs(y*y-k) >= epsilon:
        y = y - (((y**2) - k)/ (2*y))
        count +=1
    print count, "loops"
    return y
    
print newton_sqrt(1000)       