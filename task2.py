my_list = ['в', '5', 'часов', '17', 'минут', 'температура',
           'воздуха', 'была', '+5', 'градусов']

for i in range(len(my_list)):
    element = my_list[i]
    marker = element.isdigit()
    if marker:
        value = int(element)
        my_list[i] = ('{:0>2d}'.format(value))
        my_list[i] = f'"{my_list[i]}"'
    else:
        value_aux = ''
        for s in element:
            marker_symbol = s.isdigit()
            if marker_symbol:
                value = int(s)
                symbol = ('{:0>2d}'.format(value))
                s = str(symbol)
            value_aux += s
            if marker_symbol:
                my_list[i] = f'"{value_aux}"'

answer = ''
for i in range(len(my_list)):
    answer = answer + my_list[i] + ' '
print(answer)


