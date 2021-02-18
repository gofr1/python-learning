from datetime import date, datetime, timedelta


def timestamp(s):
    """Convert timestamp string to datetime"""
    return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')

trades = [
    {
        'time': timestamp('2020-05-01T13:23:32'),
        'symbol': 'AAPL',
        'volume': 100,
        'price': 310.13,
        'buy': True,
    },{
        'time': timestamp('2020-05-01T15:17:26'),
        'symbol': 'MSFT',
        'volume': 20,
        'price': 184.69,
        'buy': False,
    }
]