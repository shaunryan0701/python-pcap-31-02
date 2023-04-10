from datetime import date, datetime

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


dt = datetime(2019, 11, 4, 14, 53)

print("Datetime:", dt)
print("Date:", dt.date())
print("Time:", dt.time())

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())