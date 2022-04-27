import requests


def file_work(address):
    response = requests.get(address)
    with open('file_name.txt', 'wb') as f:
        f.write(response.content)
    with open('file_name.txt', 'r') as f:
        ip_search = {}
        result_list = []
        current_str = f.readline()
        while current_str:
            result_list.append(current_str[0:current_str.find(' - - '):])
            if not ip_search.__contains__(current_str[0:current_str.find(' - - '):]):
                ip_search[current_str[0:current_str.find(' - - '):]] = 1
            else:
                ip_search[current_str[0:current_str.find(' - - '):]] = \
                    ip_search.get(current_str[0:current_str.find(' - - '):]) + 1
            current_str = f.readline()
        spammers_addresses_list = []
        # print("Spammer's address:", max(IP_search, key=IP_search.get))
        max_request = ip_search[max(ip_search, key=ip_search.get)]
        # print(max_request)
        for key, value in ip_search.items():
            if value == max_request:
                spammers_addresses_list.append(key)

    return spammers_addresses_list


if __name__ == '__main__':

    print("Spammer's addresses:", *file_work('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'))
