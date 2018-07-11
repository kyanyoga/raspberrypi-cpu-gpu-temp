# raspberrypi-cpu-gpu-temp
A set up python scripts used to get RaspberryPi 0 or 0W GPU and CPU temperature

## usage
python bin/gettemp.py [ This will print CPU and GPU temperature ]

### raspberrypi - elasticsearch - swapi **pushing temperatures into index**
install and configure simple elasticsearch cluster
https://gist.github.com/jpalala/ab3c33dd9ee5a6efbdae

verify cluster is running with...
python bin/req.py 

load some data from swapi...
python bin/swimp.py

push real-time raspberry pi data with python into elasticsearch...
python bin/pushtempes.py

### Notes
Only tested on RaspberryPi 0 and W.
