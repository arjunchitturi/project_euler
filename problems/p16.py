#! usr/bin/env python
'''
http://projecteuler.net/problem=16
2power15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2power1000?
Answer: 1366
'''
def sum_digits(num):
    sum = 0
    while num > 0:
        sum = sum + (num % 10)
        num = num / 10
    return sum

print sum_digits(pow(2,1000))
