#!/usr/bin/env python3

import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')

# errorInfo.txt file will be created with:
#* Traceback (most recent call last):
#*   File "<stdin>", line 2, in <module>
#* Exception: This is the error message.