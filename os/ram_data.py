#!/usr/bin/env python3

import psutil
from tabulate import tabulate

class MemoryUsageDetails(object):
    
    def __init__(self):
        self.vm = psutil.virtual_memory()
        self.swap = psutil.swap_memory()

    def get_info(self):
        # memory details
        info = [{
            "Type": "RAM",
            "Total": get_size(self.vm.total),
            "Available": get_size(self.vm.available),
            "Used": get_size(self.vm.used),
            "Percentage": str(self.vm.percent)
        },
        # swap details
        {
            "Type": "SWAP",
            "Total": get_size(self.swap.total),
            "Available": get_size(self.swap.free),
            "Used": get_size(self.swap.used),
            "Percentage": str(self.swap.percent)
        }]
        return info

    def __repr__(self):
        mem = tabulate(self.get_info(), headers="keys", tablefmt="pretty")
        return mem


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f'{bytes:.2f}{unit}{suffix}'
        bytes /= factor


if __name__ == '__main__':
    print(MemoryUsageDetails())