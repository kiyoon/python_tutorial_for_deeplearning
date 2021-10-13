from functools import lru_cache
#from functools import cache

@lru_cache(maxsize=5)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


fib_cache = {}
def fib_fast(n):
    if n in fib_cache.keys():
        return fib_cache[n]
    else:
        if n <= 1:
            result = n
        else:
            result = fib_fast(n-1) + fib_fast(n-2)

        fib_cache[n] = result
        return result 


def main():
    for i in range(35):
        print(f'fib({i}) = {fib(i)}')
    for i in range(35):
        print(f'fib_fast({i}) = {fib_fast(i)}')
    print("done")


if __name__ == '__main__':
    main()
