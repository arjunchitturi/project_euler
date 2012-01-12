#! usr/bin/env python
'''
http://projecteuler.net/problem=12
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
Solution: The value is obtained by representing the triangular number as,
          product of primes raised to the power of times the prime. i.e., ax + by + ...+ cz = triangular_number.
          where, x,y,z are powers of prime numbers a,b,c respectively.
          Then, number of divisors is (x+1)(y+1)...(z+1)
Answer: 76576500
'''
#map to hold a given triangular as (ax+by+..cz) described above.
map_of_factors = {}

#this method returns a map of primes and their exponents.
def prime_factors(num):
    prime = 2
    #every number is a divisor of itself.
    map_of_factors[num] = 1
    while (prime * prime < num):
        exponent = 0
        #calculate the exponent of prime.
        while not num % prime:
            num = num / prime
            exponent = exponent + 1
        map_of_factors[prime] = exponent
        prime = prime + 1
    return map_of_factors.values()

def no_of_divisors(num):
    exponents = prime_factors(num)
    number_of_divisors = 1
    for exponent in exponents:
        if exponent:
            number_of_divisors = number_of_divisors * (exponent + 1)
    return number_of_divisors

#start from 8 as they said it has 6 divisors anyway(example) :)
for i in xrange(8, 50000):
    tri = i * (i + 1) / 2
    #clear the previous map
    map_of_factors = {}
    number_of_divisors = no_of_divisors(tri)
    if number_of_divisors > 500:
        print 'number: ', i, '\ndivisor count: ', number_of_divisors
        print 'triangular number: ', tri, '\nmap: ', map_of_factors
        '''
        veri = 1
        for k, v in map_of_factors.iteritems():
            veri = veri * pow(k, v)
        if veri == tri:
            print 'verified'
        '''
        break
