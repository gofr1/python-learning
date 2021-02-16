#!/usr/bin/env python3
import os
os.chdir('./serialization/json')

import logs_sample as ls
from logs_def import default
import json

for log in ls.logs:
    data = json.dumps(ls.asdict(log), default = default)
    print(data)

#* {"time": "2020-12-03T10:19:34.000783", "ip": "163.206.89.4", "path": "/images/cat.png", "status": 200}
#* {"time": "2021-01-13T09:12:40.000521", "ip": "165.227.94.117", "path": "/images/dog.png", "status": 200}