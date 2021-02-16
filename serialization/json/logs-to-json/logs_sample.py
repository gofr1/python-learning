#!/usr/bin/env python3
from dataclasses import dataclass, asdict
from datetime import datetime
from http import HTTPStatus
from ipaddress import IPv4Address

@dataclass
class Log():
    time: datetime
    ip: IPv4Address
    path: str
    status: HTTPStatus

logs = [
    Log (
        datetime(2020, 12, 3, 10, 19, 34, 783),
        IPv4Address('163.206.89.4'),
        '/images/cat.png',
        200
    ),
    Log (
        datetime(2021, 1, 13, 9, 12, 40, 521),
        IPv4Address('165.227.94.117'),
        '/images/dog.png',
        200
    )
]