src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
check_src = [src[0] + 1]
# print(type(check_src))
# print(src)
check_src.extend(src)
#print(check_src)

values_list = [num for num, check_num in zip(src, check_src)
                if num > check_num]
print(values_list)
