import requests
import json
from config import keys

class Convertion_Exception(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise Convertion_Exception('Данной валюты нет в базе данных.\nАктуальные валюты: /values')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise Convertion_Exception(f'Данной валюты нет в базе данных.\nАктуальные валюты: /values')

        if quote == base:
            raise Convertion_Exception('Нельзя конвертировать валюту в эдентичную валюту')

        try:
            amount = float(amount)
        except ValueError:
            raise Convertion_Exception(f'Введите корректно кол-во {quote_ticker} для конвертирования')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

        total_base = json.loads(r.content)[keys[base]]
        total_base = total_base * amount

        return total_base