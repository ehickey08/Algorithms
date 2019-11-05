#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache={}):
    if n <= 1: return 1
    if n not in cache:
        count = 0
        for i in range(1, 4):
            if n - i >= 0:
                count += eating_cookies(n - i)
        cache[n] = count
    return cache[n]


print(eating_cookies(50))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(
            "There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
                ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
