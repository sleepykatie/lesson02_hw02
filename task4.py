from functools import wraps


def third_dec(callback):
    def one_more_function(func):
        print('This is function', func)

        @wraps(func)
        def value_checker(*args):
            print('args:', args)
            # print('kwargs:', kwargs)
            for arg in args:
                if callback(arg) == False:
                    raise ValueError(f'Wrong value {arg}')
                else:
                    print(func(*args), 'Type of result calc function:', type(func(*args)))

            print('*' * 15)

        return value_checker

    return one_more_function


@third_dec(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
b = calc_cube(-5)
