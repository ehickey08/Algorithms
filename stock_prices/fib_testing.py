#top down
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

#bottom up
def fib_bottom(n):
    fib_cache = [0, 1]
    for i in range(2, n + 1):
        fib_cache.append(fib_cache[i-1] + fib_cache[i-2])

    return fib_cache


#print(fib(200))

print(fib_bottom(50))

#formula:
