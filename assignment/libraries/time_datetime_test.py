import time
import datetime
# time
print(time.ctime())

#paused time
for i in range(10):
    print("hello",i+1)
    #time.sleep(2)


#importing date 
print(datetime.date.today())
print(datetime.date.today().year)
print(datetime.date.today().month)
print(datetime.date.today().day)


#for date and time both
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)



#timegap
d=datetime.datetime(2000,5,3)
delta=datetime.timedelta(days = 30)
print("time delta")
print(d+delta)

