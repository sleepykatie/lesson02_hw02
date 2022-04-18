'''
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
"И": ["Иван", "Илья"], #random_dict["I"] = []
"М": ["Мария"],        #random_dict["I"].append('Ivan')
"П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется
сортировка по ключам? Можно ли использовать словарь в этом случае?
'''


def thesaurus(*names):
    # YOUR CODE HERE
    # random_dict = {}
    # for name in names:
    #     key_letter = name[0]
    #     if random_dict.__contains__(key_letter):
    #         random_dict[key_letter].append(name)
    #     else:
    #         random_dict.setdefault(key_letter, [name])
    #
    # return random_dict  # YOUR CODE HERE

    random_dict = {}
    for name in names:
        key_letter = name[0]
        if not random_dict.__contains__(key_letter):
            name_it = filter(lambda name: key_letter == name[0], names)
            random_dict.setdefault(key_letter, list(name_it))

    return random_dict  # YOUR CODE HERE


def thesaurus_sorted(*names):
    # YOUR CODE HERE
    random_dict_sorted = {}
    key_list = []
    for name in names:
        key_letter = name[0]
        if not key_list.__contains__(key_letter):
            key_list.append(key_letter)
    key_list.sort()
    for key_letter in key_list:
        name_it = filter(lambda name: key_letter == name[0], names)
        random_dict_sorted.setdefault(key_letter, list(name_it))

    return random_dict_sorted


def thesaurus_print(*names):
    random_dict = {}
    for name in names:
        key_letter = name[0]
        if not random_dict.__contains__(key_letter):
            name_it = filter(lambda name: key_letter == name[0], names)
            random_dict.setdefault(key_letter, list(name_it))
    key_list = list(random_dict.keys())
    key_list.sort()
    for key in key_list:
        print(key, ':', random_dict[key])


if __name__ == "__main__":
    print(thesaurus("Иван", "Мария", "Петр", "Илья", "Афанасий", 'Авдотья'))

# "Как поступить, если потребуется сортировка по ключам?" -
# т.к. созданный словарь не сортируется, сортированный словарь нужно создать?
    print(thesaurus_sorted("Иван", "Мария", "Петр", "Илья", "Афанасий", 'Авдотья'))
# или можно из созданного словаря распечатать пары ключ:значение,
# отсортированные по ключу, а в самом словаре они будут не по порядку?

    thesaurus_print("Иван", "Мария", "Петр", "Илья", "Афанасий", 'Авдотья')
