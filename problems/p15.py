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
#Memoize a.k.a Cache.
class Cached:
    ''' 
        Cache(function): an instance to memorize non-mutable arguments(keys).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        '''
        if not self.cache.has_key(args):
            self.cache[args] = self.func(*args)
        return self.cache[args]
        '''
        try: return self.cache[args]
        except KeyError:
            self.cache[args] = self.func(*args)
            return self.cache[args]

def factorial(num):
    if num <= 1:
        return num
    return factorial(num - 1) * num

fact = Cached(factorial)
print fact(40)/fact(20)/fact(20)
