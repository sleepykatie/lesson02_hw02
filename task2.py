import random
import re

random_num_list = []
for i in range(0, 30):
    num = random.randint(1, 100000)
    random_num_list.append(num)

REMOTE_ADDR_RE = re.compile(r'^\S*')
# REMOTE_ADDR_OLD_RE = re.compile(r'^(?:\d*\.\d*\.\d*\.\d*)[^\s]')
# REMOTE_ADDR_NEW_RE = re.compile(r'(?:\w{4}\:)+[^\s]')
REQ_DATETIME_RE = re.compile(r'(?<=\[)(.*)(?=\])')
REQ_TYPE_RE = re.compile(r'(?<=\]\s\")(.*)(?=\s\/)')
REQ_RESOURCE_RE = re.compile(r'(?<=\")(\w*)\s(.*)(?=\sH)')
RESP_CODE_SIZE_RE = re.compile(r'(?<=\"\s)(\d*)\s(\d*)(?=\s)')

with open('nginx_log.txt', 'r', encoding='utf-8') as f:
    text_line = f.readline()
    counter = 0
    while text_line:
        # print(text_line)
        el0_address = REMOTE_ADDR_RE.findall(text_line)
        el01_datetime = REQ_DATETIME_RE.findall(text_line)
        el02_type = REQ_TYPE_RE.findall(text_line)
        el03_resource = REQ_RESOURCE_RE.search(text_line).group(2)
        el04_code = RESP_CODE_SIZE_RE.search(text_line).group(1)
        el05_size = RESP_CODE_SIZE_RE.search(text_line).group(2)
        parsed_raw = (el0_address[0], el01_datetime[0], el02_type[0], el03_resource, el04_code, el05_size)
        for num in random_num_list:
            if num == counter:
                print(text_line)
                print(parsed_raw)
        text_line = f.readline()
        counter += 1
        #print(parsed_raw)
