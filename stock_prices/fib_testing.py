def fib_iterative(n):
    fib_cache = [0,1]
    for i in range(2, n):
        fib_cache.append(fib_cache[i-1] + fib_cache[i-2])

    return fib_cache

print(fib_iterative(500))