import sys


def users_hobby(user_names, hobby):
    user_names_list = []
    hobby_list = []
    with open(user_names, 'r', encoding='utf-8') as f:
        key = f.readline()
        while key:
            key = key.replace(',', ' ').replace('\n', '')
            user_names_list.append(key)
            key = f.readline()

    with open(hobby, 'r', encoding='utf-8') as f:
        value = f.readline()
        while value:
            value = value.replace('\n', '')
            hobby_list.append(value)
            value = f.readline()
    # print(user_names_list)
    # print(hobby_list)
    with open('users_hobby.txt', 'w', encoding='utf-8') as f:
        for i in range(len(user_names_list)):
            if len(hobby_list) > len(user_names_list):
                sys.exit(1)
            if i < len(hobby_list):
                f.writelines(f'{user_names_list[i]}: {hobby_list[i]}\n')
            else:
                f.writelines(f'{user_names_list[i]}: None\n')

    return 'users_hobby.txt'


if __name__ == '__main__':

    print(users_hobby('users.csv', 'hobby.csv'))