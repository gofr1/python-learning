#!/usr/bin/env python3
from datetime import datetime
from http import HTTPStatus
from ipaddress import IPv4Address

def default(obj):
    try:
        if type(obj) == datetime:
            return obj.isoformat()
        elif isinstance(obj, IPv4Address):
            return str(obj)
        else:
            return obj
    except:
        raise TypeError(
            "Unserializable object {} of type {}".format(obj, type(obj))
        )
