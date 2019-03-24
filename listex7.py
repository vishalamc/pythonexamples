import calendar
import datetime
month_name = datetime.date(2019, 1, 1).strftime('%B')
for month_val in range(1, 13):
    print(calendar.month_name[month_val])

