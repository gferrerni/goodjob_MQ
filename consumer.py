import requests
import json
def getConversionRates(currency):
    resp = requests.get(url=f"https://v6.exchangerate-api.com/v6/5047581ce1a477d56267e863/latest/{currency.upper()}")
    return resp.json()
    
def response(requestJSON):
    ConversionRates = getConversionRates(requestJSON["currency"])
    r = {"time": requestJSON["time"],"original_amount": requestJSON["amount"],"original_currency":requestJSON["currency"],"exchanges": []}
    for currency,exc_amount in ConversionRates["conversion_rates"].items():
    	r["exchanges"].append({"exc_amount": requestJSON["amount"]*exc_amount,"currency": currency})
    return r

