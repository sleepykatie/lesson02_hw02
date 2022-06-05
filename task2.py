class MyOwnZeroDivisionExc(Exception):
    def __init__(self, text):
        self.text = text


divisible = input('Enter the divisible: ')
divider = input('Enter the divider: ')

# try:
#     result = int(divisible)/int(divider)
# except:
#     print(MyOwnZeroDivisionExc('The divider is 0!'))
# else:
#     print('The result: ', result)

try:
    if int(divider) == 0:
        raise MyOwnZeroDivisionExc('The divider is 0!')
    result = int(divisible) / int(divider)
except MyOwnZeroDivisionExc as err:
    print(err)
else:
    print('The result: ', result)
