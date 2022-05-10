import os
import json


def file_extension(file_name):
    index = 0
    for i in range(-1, -len(file_name), -1):
        if file_name[i] == '.':
            index = i
    file_ext = file_name[(len(file_name) + index +1):len(file_name):]
    return file_ext


def folder_stat(dir_path, key_list):
    result_dict = {}
    max_size = 0
    for num in key_list:
        result_dict.update({10 ** num: (0, [])})
    # print(result_dict)
    for file in os.scandir(dir_path):
        ext_list = []
        if 10**key_list[-1] >= file.stat().st_size >= 10**key_list[-2]:
            value = list(result_dict[10**key_list[-1]])
            files_quantity = value[0] + 1
            ext = file_extension(os.path.basename(file))
            if ext_list.count(ext) == 0:
                ext_list.append(ext)
            result_dict[10 ** key_list[-1]] = (files_quantity, ext_list)
        elif 10 ** key_list[-2] > file.stat().st_size >= 10 ** key_list[-3]:
            value = list(result_dict[10 ** key_list[-2]])
            files_quantity = value[0] + 1
            ext = file_extension(os.path.basename(file))
            if ext_list.count(ext) == 0:
                ext_list.append(ext)
            result_dict[10 ** key_list[-2]] = (files_quantity, ext_list)
        elif 10 ** key_list[-3] > file.stat().st_size >= 10 ** key_list[-4]:
            value = list(result_dict[10 ** key_list[-3]])
            files_quantity = value[0] + 1
            ext = file_extension(os.path.basename(file))
            if ext_list.count(ext) == 0:
                ext_list.append(ext)
            result_dict[10 ** key_list[-3]] = (files_quantity, ext_list)
        elif file.stat().st_size < 10 ** key_list[-4]:
            value = list(result_dict[10 ** key_list[-4]])
            files_quantity = value[0] + 1
            ext = file_extension(os.path.basename(file))
            if ext_list.count(ext) == 0:
                ext_list.append(ext)
            result_dict[10 ** key_list[-4]] = (files_quantity, ext_list)
        if file.stat().st_size > max_size:
            max_size = file.stat().st_size
    if max_size > 10**key_list[-1]:
        print(f'attention, max file size more than {10**key_list[-1]}')
    return result_dict


if __name__ == '__main__':

    stat_keys = [2, 3, 4, 5]
    print(folder_stat(os.path.join(os.getcwd(), 'task4', 'some_data'), stat_keys))
    with open('some_data_summary.json', 'w') as f:
        json.dump(folder_stat(os.path.join(os.getcwd(), 'task4', 'some_data'), stat_keys), f)





