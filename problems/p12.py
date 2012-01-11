#! usr/bin/env python
'''
http://projecteuler.net/problem=12
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
def factorial(n):
    fact = 1
    for i in xrange(1, n+1): fact = fact * i
    return fact
fact = factorial(500)
x = fact
if not x % 2:
    if (i*i+i) == 2*x: print x
        x = x + 2
'''
def gcd(a,b): return b and gcd(b, a % b) or a
def lcm(a,b): return a * b / gcd(a,b)
primes = []
def get_primes(index):
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

#get_primes(1000000)
list_of_factors = {}
def factors(num):
    i = 2
    while (i * i <= num):
        count = 0
        #as long as num is divisible by i        
        while not num % i:
            num = num / i
            count = count + 1
        if i not in list_of_factors.keys(): list_of_factors[i] = count
        list_of_factors[i] = count        
        i = i + 1
    list_of_factors[num] = 1

def no_of_divisors(num):
    factors(num)
    noofdiv = 1
    for key, value in list_of_factors.iteritems():
        if value:
            noofdiv = noofdiv * (value+1)
    return noofdiv

for i in xrange(10000):
    tri = (i* (i + 1) / 2)
    list_of_factors = {}
    nodiv = no_of_divisors(tri)
    '''
    #check if they are co-prime
    if gcd(i, i+1) == 1:
        nodiv = no_of_divisors(i)*no_of_divisors(i+1)
    '''
    if nodiv > 500:
        print 'number: ', i, 'no_of_factors: ', nodiv,'\ntriangular: ', tri, 'factors: ', list_of_factors
        break
