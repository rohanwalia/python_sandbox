# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime

from time import time
from validator import validate_email

if validate_email('rohan.outlook'):
    print('success')
else :
    print('failure')

print(time())