# make sure  ES is up and running
# https://tryolabs.com/blog/2015/02/17/python-elasticsearch-first-steps/
import requests
# res = requests.get('http://101.1.10:9200')
res = requests.get('http://localhost:9200')
print res.content
