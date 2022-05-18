from functools import wraps


def first_dec(func):
    #print('This is function', func)
    @wraps(func)
    def type_logger(*args, **kwargs):
        #print('args:', args)
        #print('kwargs:', kwargs)
        result = {}
        for el in args:
            result[el] = type(el)
        for value in kwargs.values():
            result[value] = type(value)
        print("Argument's type:", result)
        print(func(*args, **kwargs), 'Type of result calc function:', type(func(*args, **kwargs)))
        print('With function name:', func.__name__, result)
        print('*' * 15)
        return func(*args, **kwargs)
    return type_logger


@first_dec
def calc_cube(x):
    return x ** 3


@first_dec
def calc_sum(x, y, z):
    return x + y + z


@first_dec
def calc_sum_named(x=0, y=0, z=0):
    return x + y + z


a = calc_cube(5)
b = calc_sum(1, 2, 3.5)
c = calc_sum_named(y=2.5, x=1.5, z=3)
