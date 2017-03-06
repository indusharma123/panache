import requests
import time
import utils




outputFile = './idmaps/climateCityIdmap'
url = "http://www.imd.gov.in/pages/city_weather_main.php"


response = requests.request("GET", url)
from BeautifulSoup import BeautifulSoup
import re


soup = BeautifulSoup(response.text)
table = soup.find('datalist')
#print table
table_body = table.findAll('option')
#print table_body
rows = map(lambda x : str(x.text.strip()),table_body)

max = 0
name = ''
FH = open(outputFile,'w')
for row in rows :
    url = "http://www.imd.gov.in/pages/city_weather_show.php"
    payload = "obs_name=%s&submit=Go" % row.replace(' ','%20')
    headers = {
        'content-type': "application/x-www-form-urlencoded"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    soup = BeautifulSoup(response.text)
    frame = soup.findAll('iframe')[0]
    soup = frame['src']
    # print soup
    try :
        id = re.search('\?id=([0-9]+)',soup).group(1)
        FH.write('%s:%s;\n' % (row, id))
    except AttributeError:
        print "cannot parse : %s " % soup # Need to log error for this










#print rows


