# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
limit = int(raw_input('Num of times: '))
position = int(raw_input('Position: ')) - 1
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
count = 0

while count < limit:
    print(tags[position].get('href', None))
    soup = BeautifulSoup(urllib.urlopen(tags[position].get('href', None)).read())
    tags = soup('a')
    count += 1
#for tag in tags:
#    print tag.get('href', None)
