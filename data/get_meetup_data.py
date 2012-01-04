import json
import urllib


def get_data(endpoint, params):
    
    url = endpoint + urllib.urlencode(params) + "&offset=%s"
    
    data = []
    offset= 0

    while True:
        response = urllib.urlopen(url%offset)
        s = unicode(response.read(), errors="ignore")
        results = json.loads(s)['results']
        if len(results) == 0:
            print "no more results returned"
            break
        data.extend(results)
        offset += 1
        print url%offset
    return data
    

params = {
    "key": "3f243d3bf32743c363b2d2e3c75d2b",
    "event_id": "43972672", # this is the event id for the intro to d3 talk
}

# get first page of members
endpoint = 'https://api.meetup.com/rsvps?' 
people = get_data(endpoint, params)

json.dump(people, open('people.json','w'))

nodes = []

profiles = []

for person in people:
    if person['response'] == "yes":
        params = {
            "key": "3f243d3bf32743c363b2d2e3c75d2b",
            "member_id": person['member_id'],
        }
        url = 'https://api.meetup.com/members?' 
        profile = get_data(url, params)[0]
        profiles.append(profile)
        if profile['photo_url'] != '':
            nodes.append({
                "name": profile['name'],
                "photo_url": profile['photo_url']
            })

json.dump(profiles, open('profiles.json','w'))

json.dump(
    {
        "nodes": nodes,
    },
    open('hackr_event.json','w')
)