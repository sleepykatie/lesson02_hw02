def odd_numbers(n):
    for num in range(1, n + 1, 2):
        yield num


if __name__ == '__main__':
    #print(odd_numbers(10))
    gen_list_odd = odd_numbers(10)
    print(next(gen_list_odd))
    print(next(gen_list_odd))
    print(next(gen_list_odd))
    #print(next(gen_list_odd))
