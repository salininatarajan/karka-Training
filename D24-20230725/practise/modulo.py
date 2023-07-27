# from datetime import date
# curr_date=date(2023,7,25)
# curr_date=date.today()
# curr_date=date.today().year
# curr_date=date.today().month
# curr_date=date.today().day
# print(curr_date)
# from datetime import time
# curr_time=time(1,30,59)
# hour=curr_time.hour
# min=curr_time.minute
# sec=curr_time.second
# print(hour)
# print(min)
# print(sec)

from datetime import datetime
# curr_datetime=datetime(2023,7,25,1,30,59)
# print(curr_datetime)
# date=curr_datetime.day
# minute=curr_datetime.minute
# print(date)
# print(minute)
# now=datetime.now()
# print(now)
# string=now.strftime("%d")
# print(string)

# from datetime import datetime
# from pytz import timezone
# format ="%Y-%m-%d %H:%M:%S"
# now_utc=datetime.now(timezone("UTC"))
# print(now_utc.strftime(format))

# now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
# print(now_asia.strftime(format))
# print(strp)
from datetime import timedelta
date_str="06 october 2000"
print(type(date_str))
strp=datetime.strptime(date_str,"%d %B %Y")
end_date=strp+timedelta(days=5)
print(end_date)














