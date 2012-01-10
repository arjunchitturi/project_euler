#! usr/bin/env python
'''
http://projecteuler.net/problem=15
Starting in the top left corner of a 2*2 grid,
there are 6 routes (without backtracking) to the bottom right corner.
How many routes are there through a 20*20 grid?
Solution: Problem gets reduced to a combinations problem:
          that is, total routes from one vertex to another vertex in any grid = (n+n)Cn
          so, 40C20
Answer: 137846528820
'''
def factorial(num):
    fact = 1
    for i in xrange(1, num+1): fact = fact*i
    return fact
f20 = factorial(20)
print factorial(40)/f20/f20
