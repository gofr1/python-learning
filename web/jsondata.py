import urllib.request
import json

def print_results(data):
    # use json module to load the string data into a dictionary
    json_data = json.loads(data)
    sep = "*"*50

    # now we can access json content
    print("\n")
    if 'title' in json_data['metadata']:
        print(json_data['metadata']['title'])

    # output the number of events
    cnt = json_data['metadata']['count']
    print(cnt, "events recorded")
    print(sep)

    # for each event print the place where it occured
    for feature in json_data['features']:
        print(feature['properties']['place'])
    print(sep)

    # print events that have magnitude greater than 4
    for feature in json_data['features']:
        if feature['properties']['mag'] >= 4.0:
            print("%2.1f" % feature['properties']['mag'], feature['properties']['place'])
    print(sep)

    # print only the events where at least 1 person reported feeling that particular event
    for feature in json_data['features']:
        felt_report = feature['properties']['felt']
        if felt_report is not None:
            if felt_report > 0:
                print("%2.1f" % feature['properties']['mag'], feature['properties']['place'], 
                "reported", feature['properties']['felt'], "times")
    print(sep)   


def main(url):
    web_url = urllib.request.urlopen(url)
    #print("Result code:", web_url.getcode())
    
    if web_url.getcode() == 200:
        data = web_url.read()
        print_results(data)
    else:
        print('Received error, cannot parse results.')

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
main(url)