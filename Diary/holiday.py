# 祝日に関するライブラリのテスト
import calendar, jpholiday

holidays = list(map(lambda d: d[0], jpholiday.month_holidays(2021, 5)))
print(holidays)

holidays_year = jpholiday.year_holidays(2017)
print(holidays_year)
