import time
from datetime import datetime, date
d = date(2018, 2, 26, 19, 01, 00)
timestamp = time.mktime(d.timetuple())
print(timestamp)
print(datetime.fromtimestamp(timestamp))
