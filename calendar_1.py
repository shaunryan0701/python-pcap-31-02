import calendar

calendar.prcal(2023, w=3, l=1)
# print(calendar.calendar(2020))

print(calendar.month(2023, 1))
print(calendar.weekday(2020, 12, 24))

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")