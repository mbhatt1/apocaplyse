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


celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])

celery.conf.result_backend = app.config['CELERY_RESULT_BACKEND']

celery.conf.update(app.config)

"""
Args: JSON with queries
"""

@celery.task(name='make_req_to_agent', bind=True)
def request_to_agent(request_json):
    req_agent = {}
    req_agent['Queries'] = request_json['Queries']
    res = requests.post('',json=req_agent)
    return jsonify(res)

@app.route('/', methods=['POST'])
def start_request_in_background():
    req_json = request.json
    return request_to_agent.delay(req_json)

if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=5000)