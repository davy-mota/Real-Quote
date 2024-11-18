import requests



def get_currency_quote(coin_origin, coin_destination):
    link = f"https://economia.awesomeapi.com.br/last/{coin_origin}-{coin_destination}"
    request_coin = requests.get(link)
    currency = request_coin.json()[f"{coin_origin}{coin_destination}"]["bid"]
    return currency

def get_currency_quote_week(coin_origin, coin_destination):
    days = 7
    link = f"https://economia.awesomeapi.com.br/daily/{coin_origin}-{coin_destination}/{days}"
    request_coin = requests.get(link)
    str_json = request_coin.json()
    values_week = []
    for i in range(len(str_json)):
        result_week = str_json[i]["bid"]
        values_week.append(result_week)
    return values_week

def get_currency_quote_monthly(coin_origin, coin_destination):
    days = 30
    link = f"https://economia.awesomeapi.com.br/daily/{coin_origin}-{coin_destination}/{days}"
    request_coin = requests.get(link)
    str_json = request_coin.json()
    values_week = []
    for i in range(len(str_json)):
        result_week = str_json[i]["bid"]
        values_week.append(result_week)
    return values_week

def get_currency_quote_quarterly(coin_origin, coin_destination):
    days = 90
    link = f"https://economia.awesomeapi.com.br/daily/{coin_origin}-{coin_destination}/{days}"
    request_coin = requests.get(link)
    str_json = request_coin.json()
    values_week = []
    for i in range(len(str_json)):
        result_week = str_json[i]["bid"]
        values_week.append(result_week)
    return values_week

def get_currency_quote_annual(coin_origin, coin_destination):
    days = 360
    link = f"https://economia.awesomeapi.com.br/daily/{coin_origin}-{coin_destination}/{days}"
    request_coin = requests.get(link)
    str_json = request_coin.json()
    values_week = []
    for i in range(len(str_json)):
        result_week = str_json[i]["bid"]
        values_week.append(result_week)
    return values_week