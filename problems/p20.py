#! usr/bin/env python
'''
http://projecteuler.net/problem=20
Find the sum of the digits in the number 100!
Answer: 648
'''
def sum_digits(n):
    s = 0
    while n > 0:
        #decrement one place value each time
        s = s + (n % 10)
        n = n / 10
    return s

n = 1
for i in xrange(1,101):
    n = n*i
print sum_digits(n)
