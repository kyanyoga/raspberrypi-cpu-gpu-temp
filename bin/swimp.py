#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Written By: Gus Segura - Blueskymetrics.com
   Get Starwars data from swapi and load into local es index
"""

# let's interate through the starwars data
from elasticsearch import Elasticsearch

# create connection to elasticsearch running locally
es = Elasticsearch([{'host':'192.168.1.10', 'port': 9200}])

# imports for handling json and web requests
import json
import requests

# create request get to es
r = requests.get('http://192.168.1.10:9200')

# set counter
i = 1

while r.status_code == 200:
    print ('...indexing St@rw@rs data...')
    r = requests.get('http://swapi.co/api/people/' + str(i))
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    i=i+1

print('data indexed-id:%d' % (i))
