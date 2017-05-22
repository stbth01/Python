import urllib
import xml.etree.ElementTree as ET
import json


while True:
    url = raw_input('Enter URL: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data

    info = json.loads(data)
    print 'User count:', len(info)
    Count = 0
    Sum = 0


    for item in info['comments']:
        Sum += int(item['count'])

        Count += 1

    print(Sum)
