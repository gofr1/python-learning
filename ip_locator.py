#!/usr/bin/env python3

from urllib import request
import json


def main():
    try:
        data = json.load(request.urlopen('http://ipinfo.io/json'))
    except Exception as e:
        print(e)
    else:
        print('You are near: {city}, {region}, {country}'.format(**data))
        print('Lat/Lng: {}E'.format(data['loc'].replace(',','N, ')))

if __name__ == '__main__':
    main()