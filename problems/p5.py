#! usr/bin/env python
'''
http://projecteuler.net/problem=5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
Answer: 232792560
'''
def gcd(a,b): return b and gcd(b, a % b) or a
def lcm(a,b): return a * b / gcd(a,b)

num = 1
for i in xrange(1, 21):
    num = lcm(num, i)
print num
