#!/usr/bin/env python3

import subprocess
import requests
import configparser

def gen_wifi_list(data:str):
    '''Generate list of WiFi Access Points'''
    wifis = []
    for line in str(data).split('\n'):
        wifi = []
        item = line.split(' ')
        for elem in item:
            if elem != '':
                wifi.append(elem)
        wifis.append(wifi)
    return wifis[1::]
    
def gen_url():
    '''Generate URL with API key'''
    config = configparser.ConfigParser()
    config.read("./.env/api.conf")
    api_key = config.get('Google Keys', 'GeoKey')
    return f'https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}'

def gen_payload():
    '''Generating payload to Google Geolocation API'''
    payload = {'considerIP': 'true'}
    try:
        cmdout = subprocess.getoutput('nmcli -f=BSSID,CHAN,SIGNAL dev wifi')
        wifi_list = gen_wifi_list(cmdout)
        if len(wifi_list) == 0:
            raise ValueError(f'No WiFi Access Points was found...')
    except Exception as e:
        print(e)
    else:
        wifiAccessPoints = []
        for wifi in wifi_list:
            wifiAccessPoints.append({
                'macAddress': wifi[0],
                'signalStrength': int(int(wifi[2]) / 2 - 100),
                'channel': int(wifi[1])
            })
        payload['wifiAccessPoints'] = wifiAccessPoints
    finally:
        return payload

def main():
    try:
        api_url = gen_url()
        payload = gen_payload()
        response = requests.post(api_url, json=payload)
        data = response.json()
        if 'error' in data.keys():
            raise requests.RequestException('Error {0}: {1}'.format(data['error']['code'], data['error']['message']))
    except Exception as e:
        print(e)
    else:
        lat = data['location']['lat']
        lng = data['location']['lng']
        accuracy = data['accuracy']
        print(f'You are within {accuracy}m of {lat}N {lng}E')

if __name__ == '__main__':
    main()

