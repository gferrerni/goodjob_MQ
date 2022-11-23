from exchange_broker import exchange_broker
import sys
import time
ntp = int(round(time.time() * 1000))
amount = float(sys.argv[1])
currency = sys.argv[2]
message = exchange_broker.delay({"time":ntp,"amount":amount,"currency": currency})
print(message)
