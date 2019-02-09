from TempWorker import app, request_to_agent
#Install celery/Flower and redis==2.10.6
#Run Flower celery -A TempWorker.celery flower -l info
#Run celery celery -A TempWorker.celery worker -l info --purge


@app.route('/', methods=['GET'])
def start_request_in_background():
    #req_json = request.json
    request_to_agent.delay()
    return 'task started'

if __name__ == '__main__':
    app.run(threaded=False, host="0.0.0.0", port=5000)