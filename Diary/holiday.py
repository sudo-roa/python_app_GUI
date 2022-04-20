import calendar, jpholiday

holidays = list(map(lambda d: d[0], jpholiday.month_holidays(2021, 5)))
print(holidays)