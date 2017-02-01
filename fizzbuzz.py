#!/usr/bin/env python
#-*-encouding:utf-8-*-

vnos = int(raw_input("Select the number between 1 and 100"))

for x in range(1,vnos):
    if x%3== 0 and x%5==0:
        print 'fizzbuzz'
    elif x%3==0:
        print 'fizz'
    elif x%5==0:
        print 'buzz'
    else:
        print x
