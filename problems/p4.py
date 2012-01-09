#! usr/bin/env python
'''
http://projecteuler.net/problem=4
Find the largest palindrome made from the product of two 3-digit numbers.
'''
palindrome = 0
for a in xrange(999, 100, -1):
    for b in xrange(a, 100, -1):
        maybe_palindrome = a * b
        #compare if new number is greater than palindrome
        #before checking for palindrome
        if maybe_palindrome > palindrome:
            s = str(a * b)
            if s == s[::-1]:
                palindrome = maybe_palindrome

print palindrome

