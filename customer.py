import requests
import json
def getConversionRates():
    resp = requests.get(url="https://v6.exchangerate-api.com/v6/5047581ce1a477d56267e863/latest/EUR")
    return resp.json()
    
def response(requestJSON):
    r = getConversionRates()
    return r

