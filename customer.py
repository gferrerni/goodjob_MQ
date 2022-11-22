from broker import exchange_broker

 
def getCurrencies():
    resp = requests.get(url="https://v6.exchangerate-api.com/v6/5047581ce1a477d56267e863/latest/EUR")
    data = resp.json()
    
    
	
exchange_broker.delay("Valon")
