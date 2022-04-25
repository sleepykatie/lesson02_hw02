src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def unique_el_set(source):
    # у меня получилось в обеих функциях через метод .count, и вторая - короче.
    # так и должно быть?

    src_one_time = set(source)

    for number in src_one_time:
        if source.count(number) > 1:
            while source.count(number) != 0:
                i = source.index(number)
                source.pop(i)
    return source


def unique_el_list(source):

    unique_numbers = [num for num in source if source.count(num) == 1]
    return unique_numbers


if __name__ == '__main__':

    print(unique_el_list(src))
    print(unique_el_set(src))
