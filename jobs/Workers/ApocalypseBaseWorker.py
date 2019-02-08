from flask import request, jsonify, Flask 
import os, sys
import requests
import subprocess

'''
#Todo: Need a base docker image for a worker. Which would be the image from cdstelly/nugget.git
#Todo: This would be the class in the image which runs the commands on nugget. 
#DockerinDocker: Instantiate as many containers as required to speedup processing?
#This class is the basic unit of job to be scheduled. After scheduling, this class talks to the rest client which wraps nugget. Nugget processes the query on the evidence and the client returns the results back to this class. This class then proceeds to store it on redis or persistent layer or both. 
#frontend-reactJS?
''' 
class ApocaplyseBaseWorker():
	
	def __init__(self, par={}):
		'''
		validate nugget runtime parameters
		thinking rn: nugget cluster has a rest client before it
		so, IP, job_id, job_description: Dict of Jobs to be executed, store_results:T/F(if T it goes to the persistent database layer, otherwise it just stays in redis and is displayed to the user. Locally can use Kumbu messaging service.
		Job Description Dict needs to be designed. Should also have an option of creating new clusters:k8s? 
		'''
		self.nugget_params = par

	def store_case_location(self, uuid=""):
		#Check for Uuid Length and Type
		self.case_location = uuid
		return 0

#'''
#Give the user the following way to run: 
#        1. Execute nugget queries they put into the UI
#        2. Execute pre-defined templates
#               a. e.g. check volume for child pornography(could have a predefined template)
#		b. e.g. check the pcap file for tls traffic/http traffic
#		c. e.g. check the pcap file for files that were exfiltrated
#		d. e.g. check memory dump for a said process
#		e. e.g. dump the said process into a file
#'''
	def store_nugget_commands(self, queries={}):
		self.nugget_queries = queries
		if bool(self.nugget_queries):
			return -1
		else:
			return 0
#'''
#Main Module
#'''
	def run():
#		'''
#		TODO: Use the parameters to make a connection to Nugget. 
#		      1. Connect existing/ Create New Docker Containers
#		      2. The containers must have access to evidence. So shared drive? One container processes one task? A task would be one nugget command. 
#		      3. Wait till the results are done? After this send it back to redis/Persistent Database Store. From redis, the output can be displayed to the user
#		'''
		return 0




