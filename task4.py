def phrase_list(employees: list):     #через создание нового списка из элемента исходного списка
    for n in range(len(employees)):
        employee = employees[n]
        list_aux = list(employee.split())
        for i in range(len(list_aux)):
            if i == len(list_aux) - 1:
                name = list_aux[i].capitalize()
                print(f"'Привет, {name}!'")


def phrases_without_list(employees: list):    # без создания нового списка, по условию
    for emp in employees:
        name = ''
        i = -1
        while emp[i] != ' ':
            name = name + emp[i]
            i = i - 1
        name = name[::-1]
        print(f"'Привет, {name.capitalize()}!'")


def phrases_slice(employees: list):       # без создания списка, срез
    for emp in employees:
        for i in reversed(range(len(emp))):   # не получился цикл in range(len(emp), 0, -1)
            if emp[i] == ' ':
                name = emp[(i+1):]
                print(f"'Привет, {name.capitalize()}!'")
                break


if __name__ == '__main__':
    emp_list = ['Инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
    phrase_list(emp_list)
    phrases_without_list(emp_list)
    phrases_slice(emp_list)

# changes for pull request