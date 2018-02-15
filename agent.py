#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import socket
import sys, uptime
import psutil
import requests
import json
import time

if __name__ == '__main__':  # Script executed directly?
	#dictionnaire qui contien les données
	data = {}
	data["host"] = socket.gethostname()
	data["os"] = os.name
	data["uptime"] = uptime._uptime_linux()
	data["cpu"] =  psutil.cpu_percent()
	data["date"] =  time.strftime("%A %d %B %Y %H:%M:%S")
	headers = {'content-type': 'application/json'}
	#on envoie les données au serveur
	r = requests.post('http://127.0.0.1:5000/api/caracteristique',data=json.dumps(data),headers=headers)
	print "Status : "+str(r.status_code)

