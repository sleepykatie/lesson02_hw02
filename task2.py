def gen(n):
    return (num for num in range(1, n + 1, 2))


if __name__ == '__main__':

    odd_generator = gen(10)
    print(type(odd_generator))
    print(next(odd_generator))
    print(next(odd_generator))
    print(next(odd_generator))
    #print(next(odd_generator))
