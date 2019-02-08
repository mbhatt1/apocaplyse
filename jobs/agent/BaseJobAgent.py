from flask import request, jsonify, Flask 
import os, sys
import requests
import subprocess


"""Rest Client interfacing with DSL
   TODO: Group queries together?
         Create Multiple containers?
"""

app = Flask(__name__)

"""Test endpoint

Returns:
    String -- Test to check if REST client is working or not
"""

@app.route('/')
def test():
    return 'Test Works'

"""Execute Endpoint
Input: 
    JSON: 
    {'CaseID' : caseID,
     'StoreResuts': T/F,
     'Queries' : []
     }


Returns:
    JSON -- Fields indexed by their queries
"""

@app.route('/execute', methods=['POST'])
def execute():
    req_json = request.json 
    outputs = {}
    #start a subprocess with nugget
    proc = subprocess.Popen('/nugget/nugget -interactive', stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    #Iterate through and execute queries
    for query in req_json['Queries']:
        proc.stdin.write(query+'\n')
        outputs[query] = proc.stdout.read()
    #kill the process
    proc.stdin.close()
    proc.kill()
    return jsonify(outputs)


if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=5000)





