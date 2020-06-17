#!/usr/bin/env python3

import uuid

mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8*6, 8)][::-1])
print(f'Your MAC address in formatted way is: {mac_address}')