import requests
from BeautifulSoup import BeautifulSoup

inputFile = './idmaps/climateCityIdmap'
outputFile = './output/tempratureMapx'
try :
    FH = open(inputFile,'r')
    FO = open(outputFile, 'w')
except IOError:
    print "input file not present : %s " % inputFile

cityIdMap = {}
for line in FH :
    name,id = line.split(':')
    cityIdMap[name] = id.rstrip(';').replace(' ','%20')



for name in cityIdMap :
    tempMap = {}
    url = 'http://14.139.247.11/citywx/city_weather.php?id=%s' % cityIdMap[name]
    response = requests.request("POST", url)
    soup = BeautifulSoup(response.text)
    print response.text
    body = soup.find('body')
    try :
        table = body.find('table').findAll('table')[1]
        counter = 0
        for row in table.findAll('tr'):
            tempMap[counter] = row.findAll('td')
            counter += 1
        #print tempMap
        tempMap = map(lambda (x, y): (x, [str(element.text) for element in y]), tempMap.iteritems())
        FO.write('%s:%s\n' % (name,str(tempMap[2][1])))
    except AttributeError :
        print 'error paring data for %s' % name
        print 'debug data : %s' % body

    exit(1)