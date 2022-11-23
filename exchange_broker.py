from celery import Celery
from customer import response

broker_url = "amqp://localhost"
redis_url = "redis://localhost"
app = Celery('tasks', broker=broker_url, backend=redis_url)

@app.task
def exchange_broker(requestJSON):
    r = response(requestJSON)
    print("recibido! Calculando...")
    print(r)
    return f"{r}"
	
