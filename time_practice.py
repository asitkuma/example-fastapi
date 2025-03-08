from datetime import datetime
# import time

str="2025-02-20 11:42:50.697874+05:30"
date,today_time=str.split(" ")
now_time,second=today_time.split(".")

whole_date=datetime.strptime(date,"%Y-%m-%d")
month_name=whole_date.strftime("%B")
day_name=whole_date.strftime("%A")
year=whole_date.year
print(month_name,day_name,year)