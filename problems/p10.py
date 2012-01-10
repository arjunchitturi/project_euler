#! usr/bin/env python
'''
http://projecteuler.net/problem=10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
This problem is similar to p7. only need to add the primes.
Answer: 142913828922
'''
index = 2000000
primes = [2]
num = 3
while num <= index:
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
print sum(primes)
