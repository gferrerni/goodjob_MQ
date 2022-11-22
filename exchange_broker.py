from celery import Celery
import requests

broker_url = "amqp://localhost"
redis_url = "redis://localhost"
app = Celery('tasks', broker=broker_url, backend=redis_url)


@app.task
def exchange_broker(json: str):
    return f"{json}"
	
