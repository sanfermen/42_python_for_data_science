import datetime

today = datetime.date.today()
first = datetime.datetime(1970, 1, 1)
date = today
time = (today - first.date()).total_seconds()
# Convert in scientific notation
sc_not = "{:e}".format(time)

print(f"Seconds since January 1, 1970: {time:,}")
print(f"or {sc_not} in scientific notation")
print(date)