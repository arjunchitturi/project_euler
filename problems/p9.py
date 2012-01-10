#! usr/bin/env python
'''
http://projecteuler.net/problem=9
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
Solution:Using the two inequations a2 + b2 = c2 ----(1)
                                   a + b + c = 1000 (2)
                              and, a < b < c -------(3)
        Here the problem gets reduced to:
        a*b == 1000*(500-c)
        Otherwise, we have c*C = a*a + b*b which uses more calculation.
Answer: 31875000
'''
for a in xrange(1,1000):
    for b in xrange(a,1000):
        c = 1000 - a - b
        if a*b == 1000*(500-c):
            print a*b*c
