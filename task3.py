class IntListError(Exception):
    def __init__(self, text):
        self.text = text


result_list = []
inp_data = 0

while inp_data != 'stop':
    inp_data = input('Enter an integer: ')
    if inp_data.casefold() == 'stop':
        break
    try:
        if not inp_data.isdigit():
            if inp_data[0] != '-':
                raise IntListError('Enter only digits!')
        result_list.append(int(inp_data))
    except IntListError as err:
        print(err)
print('List of numbers: ', result_list)
