#! usr/bin/env python
'''
http://projecteuler.net/problem=7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
Solution: 'n' is a prime number if the list of primes under square root of 'n' do not divide 'n'.
Answer: 104743
'''
index = 10001
primes = []
primes.append(2)
num = 3
while len(primes) < index:
    dont_add = False
    for prime in primes:
        if prime*prime > num:
           break
        #check for a composite number
        if not num % prime:
           dont_add = True
           break
    if dont_add is False:
        primes.append(num)
    num = num + 1
print primes[len(primes)-1]
