from fredapi import Fred
from keys import *

fred = Fred(APIKEY)
data = fred.get_series_all_releases('GDPPOT')
print(data)