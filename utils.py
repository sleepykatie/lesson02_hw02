import requests
import xml.etree.ElementTree as ET
from datetime import datetime


def currency_rates_fl(currency_code):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    root = ET.fromstring(response.text)
    current_date = root.attrib['Date']
    current_date_object = datetime.strptime(current_date, '%d.%m.%Y')
    current_date_object = current_date_object.strftime('%d.%m.%Y')
    #print(type(current_date_object))
    for child in root:
        if child[1].text == currency_code.upper():
            currency_value = float(child[4].text.replace(',','.'))
            #print(type(currency_value))

            return f'{currency_code.upper()}: {currency_value} ₽ на {current_date_object}'


if __name__ == '__main__':

    print('result - float')
    print(currency_rates_fl('uSd'))
    print(currency_rates_fl('euR'))

