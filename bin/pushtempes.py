#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Written By: Gus Segura - Blueskymetrics.com
   Push RaspberryPI CPU and GPU temperatures to elasticsearch
"""

from __future__ import division
from datetime import datetime
from elasticsearch import Elasticsearch
import uuid
import time
import gettemp
import csv

# create a connection to es
es = Elasticsearch([{'host':'192.168.1.10', 'port': 9200}])

# create index - ignore 400 
es.indices.create(index='sensor', ignore=400)

# sensor id
ssid = "0010"

# index some data
if __name__ == "__main__":
	# print("...Starting...")
	while(True):
		# get id and metrics
		ides 	= uuid.uuid4().hex
		cpues 	= gettemp.getcput()
		gpues	= gettemp.getgput()
		tses	= datetime.now()
		# index metrics into  es
		es.index(index="sensor", doc_type="test-type",
			 id=ides,
		 	 body={"sens":ssid,
			       "cpu":cpues, 
			       "gpu":gpues, 
			       "ts":tses})
		# debug
		# print ("uuid:%s ts:%s cpu:%f gpu:%f" % (ides,tses,cpues,gpues))
		#print (es.get(index="my-index", doc_type="test-type", id=1)['_source']) 
		#print gettemp.getgput()

		# log data to csv
		row = [tses, ides, ssid, cpues, gpues]
		with open('templog.csv', 'a') as f:
			w = csv.writer(f)
			w.writerow(row)
		
		# wait an interval
                time.sleep(900)
