'''
*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр
Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
        },
    "И": {
        "И": ["Илья Иванов"]
        },
    "С": {
            "И": ["Иван Сергеев", "Инна Серова"],
            "А": ["Анна Савельева"]
        }
}
Как поступить, если потребуется сортировка по ключам?
'''


def thesaurus(*fullnames):
    # YOUR CODE HERE
    random_dict = {}
    key_s_list = []

    def surname_key(fullname):
        fullname_as_list = fullname.split()
        surname = fullname_as_list[1]

        return surname[0]

    for fullname in fullnames:
        key_letter = surname_key(fullname)
        if not random_dict.__contains__(key_letter):
            key_s_list.append(key_letter)
    key_s_list.sort()

    for key_letter in key_s_list:
        for fullname in fullnames:
            key_s = surname_key(fullname)
            if key_s == key_letter:
                if not random_dict.__contains__(key_s):
                    fullname_it = filter(lambda fullname: key_s == surname_key(fullname), fullnames)
                    fullname_list = list(fullname_it)
                    surname_letter_dict = {}
                    for el in fullname_list:
                        key_n = el[0]
                        if not surname_letter_dict.__contains__(key_n):
                            name_it = filter(lambda el: key_n == el[0], fullname_list)
                            surname_letter_dict.setdefault(key_n, list(name_it))
                    random_dict.setdefault(key_s, surname_letter_dict)

    return random_dict # YOUR CODE HERE


if __name__ == "__main__":
    print(thesaurus("Иван Сергеев", "Инна Серова",
                    "Петр Алексеев", "Илья Иванов", "Анна Савельева"))