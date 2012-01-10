import json
import urllib
from operator import itemgetter


def get_data(endpoint, params):
    
    url = endpoint + urllib.urlencode(params) + "&offset=%s"
    
    data = []
    offset= 0

    while True:
        print url%offset
        response = urllib.urlopen(url%offset)
        s = unicode(response.read(), errors="ignore")
        try:
            results = json.loads(s)['results']
        except KeyError:
            print s
            raise IOError("something went wrong...")
        if len(results) == 0:
            print "no more results returned"
            break
        data.extend(results)
        offset += 1
    return data

params = {
    "key": "3f243d3bf32743c363b2d2e3c75d2b",
    "group_urlname": "nyhackr",
    "status":"past"
}

# get first page of members
endpoint = 'https://api.meetup.com/2/events?' 
meetups = get_data(endpoint, params)
meetups.sort(key=itemgetter('time'))
json.dump(meetups, open("meetup_history.json",'w'))
