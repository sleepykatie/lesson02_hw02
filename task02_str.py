import requests
import decimal

def currency_rates_dec(currency_code):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    response_text = response.text
    #print(type(response_text))
    currency_code_index = response_text.find(currency_code.upper())

    if currency_code_index == -1:
        return None
    else:
        data = response_text[currency_code_index::]
        my_value = data[(data.find('<Value>') + len('<Value>')):data.find('</Value>'):]
        return decimal.Decimal(my_value.replace(',', '.'))


if __name__ == '__main__':

    print('result - decimal')
    print('USD: ', currency_rates_dec('uSd'))
    print('EUR: ', currency_rates_dec('euR'))
    print('AUD: ', currency_rates_dec('hhh'))
