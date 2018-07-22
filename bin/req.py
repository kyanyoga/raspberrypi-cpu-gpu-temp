#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Written By: Gus Segura - Blueskymetrics.com
   Verify connection to local elasticsearch cluster with python.
"""

# make sure  ES is up and running
# https://tryolabs.com/blog/2015/02/17/python-elasticsearch-first-steps/
import requests
res = requests.get('http://192.168.1.10:9200')
#res = requests.get('http://localhost:9200')
print res.content
