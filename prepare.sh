python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt

docker-compose up -d
docker ps

celery -A tasks worker -l info --pool=solo
