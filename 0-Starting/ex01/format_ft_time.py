from datetime import datetime

today = datetime.today()
first = datetime(1970, 1, 1)
date = today.date()
time = (today - first).total_seconds()
#Convert in scientific notation
sc_not = "{:e}".format(time)

print(f"Seconds since January 1, 1970: {time:,} or {sc_not} in scientific notation")
print(date)