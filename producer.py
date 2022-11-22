from tasks import exchange_broker
import sys
import time
ntp = int(round(time.time() * 1000))
amount = float(sys.argv[1])
currency = sys.argv[2]
message = exchange_broker.delay("{'time':%i,'amount':%.2f,'original_currency': '%s'}"%(ntp,amount,currency))
print(message)
