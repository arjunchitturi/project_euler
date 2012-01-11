#! usr/bin/env python
'''
http://projecteuler.net/problem=17
How many letters would be needed to write all the numbers in words from 1 to 1000?
Answer: 21124
'''
#map of number and the corresponding word in english count
words = { 0:0, 1:3, 2:3, 3: 5, 4: 4, 5: 4, 6: 3, 7:5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, \
17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 8 }
count = 0

for i in xrange(1, 1001):
    a = str(i)
    l = len(a)
    if l == 4:
        count = count + words[1000]
        count = count + words[1]
        break
    if l == 3:
        count = count + words[100] # for the word 'hundred'
        count = count + words[i / 100] # for the word before 'hundred'
        #check multiple of hundred
        if not i % 100:
            continue
        count = count + 3 # for the word 'and'
        i = i % 100
        a = str(i)
        l = len(a)
    if l == 2:
        if words.has_key(i):
            count = count + words[i]
        else:
            n = i / 10
            count = count + words[n*10] # for the words 'twenty' in (21 - 29),.,'ninety' in (91 - 99)
            i = i % 10
            a = str(i)
            l = len(a)
    if l == 1:
        count = count + words[i]

print count
