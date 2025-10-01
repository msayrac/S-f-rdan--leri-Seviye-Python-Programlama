
from datetime import datetime
from datetime import timedelta
# import datetime

# result =dir(datetime)

simdi = datetime.now()

print(simdi)
print(simdi.today())

print(simdi.year)
print(simdi.month)
print(simdi.hour)
print(simdi.minute)
print(simdi.second)

result = datetime.ctime(simdi)
print(result)

print(datetime.strftime(simdi,"%Y"))
print(datetime.strftime(simdi,"%X"))
print(datetime.strftime(simdi,"%d"))
print(datetime.strftime(simdi,"%A"))
print(datetime.strftime(simdi,"%B"))

print(datetime.strftime(simdi,"%Y %B %A"))

t = "15 April 2019 hour 10:12:30"

result = datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
print(result)

print(result.year)

birthday = datetime(1983,5,19, 12,30,10)

print(birthday)

result = datetime.timestamp(birthday)

print(result)

result =datetime.fromtimestamp(result)
print(result)

result = datetime.fromtimestamp(0)
print(result)

result = simdi -birthday # time delta

result = result.days
print(simdi)
# result = simdi + timedelta(10)
result = simdi + timedelta(days=730, minutes = 10)
result = simdi -timedelta(10)
print(result)

