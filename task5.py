def order_ascend(price: list):      # B
    print(sorted(price))
    if price == basic_price_list:
        print('Список не изменился')
    else:
        print('Список изменился')
    return price


def order_descend(price: list):      #C
    price.sort(reverse=True)
    print(price)
    if price == basic_price_list:
        print('Список не изменился')
    else:
        print('Список изменился')
    return price


def price_format(price: list):   # A
    price_list_formatted = []
    for number in price:
        if type(number) == int:
            number = float(number)
        rub = number // 1
        kop = int(round((number % 1 * 100), 2))
        kop_int = ('{:0>2d}'.format(kop))
        number = f'{int(rub)} руб. {kop_int} коп.'
        price_list_formatted.append(number)
        result = ', '.join(price_list_formatted)
    return result


def highest_price(price: list):    # D
    price.sort()
    result = price[(len(price)-5):len(price)]
    return result


if __name__ == '__main__':
    basic_price_list = [57.8, 46.51, 97, 48.03, 52.78, 67.4,
                  94.3, 30, 26.86, 34.7, 74.05, 6.59, 80.04]
    price_list = [57.8, 46.51, 97, 48.03, 52.78, 67.4,
                  94.3, 30, 26.86, 34.7, 74.05, 6.59, 80.04]
    print('Task B')
    price_list_ascend = order_ascend(price_list)
    print(price_list_ascend)
    print('Task C')
    price_list_descend = order_descend(price_list)
    print(price_list_descend)
    print('Task A')
    print(price_format(basic_price_list))
    print('Task D')
    print(highest_price(basic_price_list))




