import requests


def file_work(address):
    response = requests.get(address)
    with open('file_name.txt', 'wb') as f:
        f.write(response.content)
    with open('file_name.txt', 'r') as f:
        list_of_tuple = []
        for current_str in f.readlines():
            result_list = [current_str[0:current_str.find(' - - '):],
                           current_str[current_str.find('GET'):(current_str.find('GET') + 3):],
                           current_str[current_str.find('/downloads'):current_str.find(' HTTP'):]]
            list_of_tuple.append(tuple(result_list))
    return list_of_tuple


if __name__ == '__main__':

    print(file_work('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'))
