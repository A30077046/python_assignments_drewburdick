import json
import urllib2
import sys

search = True
while (search):
    print '\033[1m' + "Please enter a zipcode or city name:";
    location = raw_input()
    url = 'https://api.apixu.com/v1/current.json?key=4d325b458216426e957151404163103&q=' + location
    jsonTxt = urllib2.urlopen(url).read()
    weather = json.loads(jsonTxt)
    
    print '\033[0m'
    print "---------------------------------------------------------------------"
    print
    print "Here is the current weather for %s, %s." % (weather["location"]["name"], weather["location"]["region"])
    print "%s and %s degrees (F)." % (weather["current"]["condition"]["text"], weather["current"]["temp_f"])
    print "Feels like %s (F)." % weather["current"]["feelslike_f"]
    print
    print "---------------------------------------------------------------------"
    
    print '\033[1m'
    print "Want to check another location? y/n";
    startOver = raw_input()
    print '\033[0m'
    print "---------------------------------------------------------------------"
    print
    
    if startOver == "n":
        print'\033[1m'
        sys.exit("Good-bye!")
