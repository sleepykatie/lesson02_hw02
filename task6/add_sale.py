import sys


def add_sale(sale):

    path_to_file = os.path.join('task6', 'bakery.csv')
    with open(path_to_file, 'a', encoding='utf-8') as f:
        f.writelines([f'{sale}\n'])


if __name__ == '__main__':

    # print(add_sale(8914.3))
    add_sale(sys.argv[1])
