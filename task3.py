import sys


def users_hobby(user_names, hobby):
    # hobby_data = {}
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
    for i in range(len(user_names_list)):
        if len(hobby_list) > len(user_names_list):
            sys.exit(1)
        if i < len(hobby_list):
            hobby_data[user_names_list[i]] = hobby_list[i]
        else:
            hobby_data[user_names_list[i]] = None
    with open('user_data.txt', 'w', encoding='utf-8') as f:
            f.writelines(str(hobby_data) + '\n')

    return hobby_data


if __name__ == '__main__':

    print(users_hobby('users.csv', 'hobby.csv'))