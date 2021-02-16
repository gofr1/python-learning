from datetime import datetime

def default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj

def pairs_hook(pairs):
    obj = {}
    for key, value in pairs:
        if key == 'purchase date':
            value = datetime.fromisoformat(value)
        obj[key] = value
    return obj