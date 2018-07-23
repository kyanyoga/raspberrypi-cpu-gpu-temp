# raspberrypi-cpu-gpu-temp
A set of python scripts used to get (gettemp.py) RaspberryPi 0 or 0W GPU and CPU temperature

## usage
python bin/gettemp.py [ This will print CPU and GPU temperature ]

### raspberrypi - elasticsearch - swapi **pushing temperatures into index**
install and configure simple elasticsearch cluster
https://gist.github.com/jpalala/ab3c33dd9ee5a6efbdae

python bin/req.py [verify cluster is running]

python bin/swimp.py [load some data from swapi]

python bin/pushtempes.py [push real-time raspberry pi data into es]

### Notes
Tested on RaspberryPi 3, RaspberryPi 0 and W.
