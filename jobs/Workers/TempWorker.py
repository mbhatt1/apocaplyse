from flask import Flask, request, jsonify
from celery import Celery
import requests

"""This file contains a thin rest client which cordinates creation of Celery tasks. Each task queries the Agent to execute 
a query. The query is executed and response is received. Response should be stored in redis as well as returned to the user. 

Args:
JSON with queries to endpoint '/'

Returns:
    JSON -- Results pertaining to each query
"""

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = make_celery(app)

celery.conf.update(app.config)

"""
Args: JSON with queries
"""

@celery.task(name='make_req_to_agent')
def request_to_agent(request_json):
    req_agent = {}
    req_agent['Queries'] = request_json['Queries']
    res = requests.post('',json=req_agent)
    return jsonify(res)

#Run Celery: celery -A TempWorker.celery worker -l info
#Run Flask: python3 FlaskClient.py
