import datetime
from dateutil.relativedelta import relativedelta

myDate = datetime.datetime(1975,8,4)
now = datetime.datetime.now()



difference = relativedelta(now, myDate)
print(difference)
