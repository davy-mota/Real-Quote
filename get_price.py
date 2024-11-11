import requests

def get_currency_quote(coin_origin, coin_destination):
    link = f"https://economia.awesomeapi.com.br/last/{coin_origin}-{coin_destination}"
    request_coin = requests.get(link)
    currency = request_coin.json()[f"{coin_origin}-{coin_destination}"]["bid"]
    return currency