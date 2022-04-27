import sys
import os


def edit_sale_full_read(number, value):

    path_to_file = os.path.join('task6', 'bakery.csv')
    with open(path_to_file, 'r', encoding='utf-8') as f:
        bakery_data = f.readlines()
        print(bakery_data)
        for i in range(len(bakery_data)):
            if i == number - 1:
                bakery_data[i] = str(value) + '\n'
        print(bakery_data)
    with open(path_to_file, 'w', encoding='utf-8') as f:
        f.writelines(bakery_data)


if __name__ == '__main__':


    edit_sale_full_read(int(sys.argv[1]), float(sys.argv[2]))