web: gunicorn --pythonpath travellife/ --bind :5736 --workers=3 travellife.wsgi
worker: celery --workdir=travellife/ --app=travellife.celery:app --concurrency=3 worker -B
flower: celery --workdir=travellife/ --app=travellife.celery:app flower
