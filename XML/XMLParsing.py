import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_342154.xml'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print( 'Retrieving', url)
    uh = urllib.urlopen(url)
    data = uh.read()
    print( 'Retrieved',len(data),'characters')
    #print(data)
    tree = ET.fromstring(data)


    counts = tree.findall('.//comment')
    count = 0
    for item in counts:
        count += int(item.find('count').text)
    #lat = results[0].find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text

    #print( 'lat',lat,'lng',lng)
    print(count)
