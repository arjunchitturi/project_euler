#! usr/bin/env python
'''
http://projecteuler.net/problem=14
The following iterative sequence is defined for the set of positive integers:

n = n/2 (n is even)
n = 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
Answer: 837799
'''
max_seq_len = 0
longest_chain_number = 1
for x in xrange(1,1000000):
    seq_len = 0
    starting_number = x
    while x != 1:
        #if x is divisible by 2
        if x % 2:
            x = 3*x + 1
        else:
            x = x / 2
        seq_len = seq_len + 1
    if max_seq_len < seq_len:
        max_seq_len = seq_len
        longest_chain_number = starting_number
print longest_chain_number 
