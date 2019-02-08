from flask import request, jsonify, Flask 
import os, sys
import requests
import subprocess

app = Flask(__name__)


@app.route('/')
def test():
    return 'Test Works'

'''
    JSON: 
    {'CaseID' : caseID,
     'StoreResuts': T/F,
     'Queries' : []
     }
'''

@app.route('/execute', methods=['POST'])
def execute():
    req_json = request.json 
    outputs = {}

    proc = subprocess.Popen('/nugget/nugget -interactive', stdout=subprocess.PIPE, stdin=subprocess.PIPE)

    for query in req_json['Queries']:
        proc.stdin.write(query+'\n')
        proc.stdin.close()
        outputs[query] = proc.stdout.read()

    proc.kill()
    return jsonify(outputs)


if __name__ == '__main__':
    app.run(threaded=True)





