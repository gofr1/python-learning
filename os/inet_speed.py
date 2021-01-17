#!/usr/bin/env python3
# Measure internet speed

import speedtest
from tabulate import tabulate

class NetworkDetails(object):
    def __init__(self):
        self.speed_parser = speedtest.Speedtest()

    def __repr__(self):
        down = str(f'{round(self.speed_parser.download()/1_000_000, 2)} Mbps')
        up = str(f'{round(self.speed_parser.upload()/1_000_000, 2)} Mbps')
        data = {
            "Download": [down],
            "Upload": [up]
        }
        table = tabulate(data, headers="keys", tablefmt="pretty")
        return table

if __name__ == '__main__':
    print(NetworkDetails())