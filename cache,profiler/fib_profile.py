from functools import cache

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


@cache
def fib_fast(n):
    if n <= 1:
        return n
    return fib_fast(n-1) + fib_fast(n-2)


def main():
    for i in range(35):
        print(f'fib({i}) = {fib(i)}')
    for i in range(35):
        print(f'fib_fast({i}) = {fib_fast(i)}')
    print("done")


if __name__ == '__main__':
    main()
