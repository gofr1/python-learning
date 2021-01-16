#!/usr/bin/env python3

import psutil

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f'{bytes:.2f}{unit} {suffix}'
        bytes /= factor

def ram_info():
    # memory details
    vm = psutil.virtual_memory()
    info = {
        "Type": "RAM",
        "Total": get_size(vm.total),
        "Available": get_size(vm.available),
        "Used": get_size(vm.used),
        "Percentage": vm.percent
    }
    return info

def swap_info():
    swap = psutil.swap_memory()
    swap_info = {
        "Type": "SWAP",
        "Total": get_size(swap.total),
        "Free": get_size(swap.free),
        "Used": get_size(swap.used),
        "Percentage": swap.percent
    }
    return swap_info

def print_info(info):
    for key, value in info.items():
        print(f'{key}: {value}')
    print("-"*20)

if __name__ == '__main__':
    print_info(ram_info())
    print_info(swap_info())
