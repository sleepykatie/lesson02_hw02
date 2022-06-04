import re
import datetime
current_date = datetime.datetime.now()

# re_date = re.compile(r'^(\d{2}-){2}\d{4}$')
#
# for date in ['23.01.1990', '12-03-1870', '9-12-784']:
#     if re_date.match(date):
#         print(date, "it's OK")
#     else:
#         print(f'Wrong date {date}')


class Date:

    def __init__(self, date_str):
        re_date = re.compile(r'^(\d{2}-){2}\d{4}$')
        if not re_date.match(date_str) and type(date_str) != str:
            raise ValueError('Wrong format!')
        else:
            self.date_str = date_str

    @classmethod
    def date_to_int(cls, date_str):
        # re_day = re.compile(r'^\d{2}')
        # re_month = re.compile(r'-\d{2}')
        # re_year = re.compile(r'-\d{4}$')
        # day = re_day.match(date_str)
        # month = re_month.match(date_str)
        # year = re_year.match(date_str)
        date_parts = date_str.split('-')
        day = int(date_parts[0])
        month = int(date_parts[1])
        year = int(date_parts[2])

        return [day, month, year]

    @staticmethod
    def date_validation(date_list):
        month_31day = [1, 3, 5, 7, 8, 10, 12]
        month_30day = [4, 6, 9, 11]
        if not 1900 <= date_list[2] <= current_date.year:
            return 'Wrong year!'
        if not 0 < date_list[1] <= 12:
            return 'Wrong month!'
        for month in month_31day:
            if month == date_list[1]:
                if not 0 < date_list[0] <= 31:
                    return 'Wrong day!'
        for month in month_30day:
            if month == date_list[1]:
                if not 0 < date_list[0] <= 30:
                    return 'Wrong day!'
        if date_list[1] == 2 and not 0 < date_list[0] <= 29:
            return 'Wrong day!'
        else:
            return 'The date is valid'


date_01 = Date('02-02-1980')
print(date_01.date_to_int('03-03-1970'))
print(Date.date_to_int('01-01-1995'))
print(Date.date_validation(date_01.date_to_int('23-12-1999')))
