def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def main():
    for i in range(40):
        print(f'fib({i}) = {fib(i)}')
    print("done")


if __name__ == '__main__':
    main()
