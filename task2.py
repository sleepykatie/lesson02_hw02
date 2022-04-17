'''
 *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
должен быть с заглавной. Например:
# >>> num_translate_adv("One")
"Один"
# >>> num_translate_adv("two")
"два"
'''


def num_translate_adv(number: str):
    # YOUR CODE HERE

    num_1_to_10 = {'one': 'один',
                   'two': 'два',
                   'three': 'три',
                   'four': 'четыре',
                   'five': 'пять',
                   'six': 'шесть',
                   'seven': 'семь',
                   'eight': 'восемь',
                   'nine': 'девять',
                   'ten': 'десять'}

    result = num_1_to_10.get(number)
    if number.istitle():
        value = num_1_to_10.get(number.casefold())
        result = value.title()

    return result   # YOUR CODE HERE

if __name__ == "__main__":

    print(num_translate_adv('One'))
    print(num_translate_adv('six'))
    print(num_translate_adv('TeN'))
