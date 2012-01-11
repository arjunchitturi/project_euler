#! usr/bin/env python
'''
http://projecteuler.net/problem=19
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
Answer: 171
'''
import datetime
sundays = 0
for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        d = datetime.date(year, month, 1)
        if d.weekday() == 6:
            sundays = sundays + 1
print sundays
