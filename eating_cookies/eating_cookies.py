#!/usr/bin/python

import sys
import time


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

#top down
def eating_cookies(n, cache={}):
    if n <= 1:
        return 1
    if n not in cache:
        count = 0
        for i in range(1, 4):
            if n - i >= 0:
                count += eating_cookies(n - i)
        cache[n] = count
    return cache[n]


#bottom up
def eating_cookies_fast(n):
    if n == 0:
        return 1
    cache = [1, 2, 4]
    if n < 3:
        return cache[n - 1]
    for i in range(3, n):
        cache.append(cache[i - 1] + cache[i - 2] + cache[i - 3])
    return cache[n - 1]

print(eating_cookies_fast(1000000))
if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(
            "There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
                ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
