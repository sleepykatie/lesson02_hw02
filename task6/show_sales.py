import sys
import os


def show_sales(start=0, end=0):
    path_to_file = os.path.join('task6', 'bakery.csv')
    if start == 0 and end == 0:
        with open(path_to_file, 'r', encoding='utf-8') as f:
            bakery_data = f.readlines()
            for line in bakery_data:
                line = line.replace('\n', '').replace('.', ',')
                print(line)
    elif start >= 0 and end == 0:
        with open(path_to_file, 'r', encoding='utf-8') as f:
            line = f.readline()
            i = 0
            while line:
                if i >= start - 1:
                    line = line.replace('\n', '').replace('.', ',')
                    print(line)
                    i = i + 1
                    line = f.readline()
                else:
                    line = f.readline()
                    i = i + 1
    elif start >= 0 and end >= 0:
        with open(path_to_file, 'r', encoding='utf-8') as f:
            line = f.readline()
            i = 0
            while line:
                if (i >= start - 1) and (i <= end - 1):
                    line = line.replace('\n', '').replace('.', ',')
                    print(line)
                    i = i + 1
                    line = f.readline()
                else:
                    line = f.readline()
                    i = i + 1


if __name__ == '__main__':

    # show_sales()
    # show_sales(3)
    # show_sales(2, 4)
    if len(sys.argv) == 1:
        show_sales()
    elif len(sys.argv) == 2:
        show_sales(int(sys.argv[1]))
    elif len(sys.argv) == 3:
        show_sales(int(sys.argv[1]), int(sys.argv[2]))
