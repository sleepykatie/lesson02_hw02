import os


def folder_stat(dir_path, key_list):
    result_dict = {}
    max_size = 0
    for num in key_list:
        result_dict.update({10 ** num: 0})
    # print(result_dict)
    for file in os.scandir(dir_path):
        if 10**key_list[-1] >= file.stat().st_size >= 10**key_list[-2]:
            result_dict[10**key_list[-1]] = result_dict[10**key_list[-1]] + 1
        elif 10 ** key_list[-2] > file.stat().st_size >= 10 ** key_list[-3]:
            result_dict[10 ** key_list[-2]] = result_dict[10 ** key_list[-2]] + 1
        elif 10 ** key_list[-3] > file.stat().st_size >= 10 ** key_list[-4]:
            result_dict[10 ** key_list[-3]] = result_dict[10 ** key_list[-3]] + 1
        elif file.stat().st_size < 10 ** key_list[-4]:
            result_dict[10 ** key_list[-4]] = result_dict[10 ** key_list[-4]] + 1
        if file.stat().st_size > max_size:
            max_size = file.stat().st_size
    if max_size > 10**key_list[-1]:
        print(f'attention, max file size more than {10**key_list[-1]}')
    return result_dict


if __name__ == '__main__':

    stat_keys = [2, 3, 4, 5]
    print(folder_stat(os.path.join(os.getcwd(), 'task4', 'some_data'), stat_keys))
