import requests
import json
def getConversionRates():
    resp = requests.get(url="https://v6.exchangerate-api.com/v6/5047581ce1a477d56267e863/latest/EUR")
    return resp.json()
    
def response(requestJSON):
    ConversionRates = getConversionRates()
    r = {"time": requestJSON["time"],"original_amount": requestJSON["amount"],"original_currency":requestJSON["currency"],"exchanges": []}
    for currency,exc_amount in ConversionRates["conversion_rates"].items():
    	print(requestJSON['amount'],"*",exc_amount)
    	r["exchanges"].append({"exc_amount": requestJSON["amount"]*exc_amount,"currency": currency})
    return r

