import calendar
import datetime

year,month,day = input("please, write your birthday in this order: year, month, day: ").split(" ")

date = datetime.date(int(year),int(month),int(day))
day_int = date.weekday()
print(day_int)
if(day_int == 0):
    print("Monday")
if(day_int == 1):
    print("Tuesday")
if(day_int == 2):
    print("Wednesday")
if(day_int == 3):
    print("Thursday")
if(day_int == 4):
    print("Friday")
if(day_int == 5):
    print("Saturday")
if(day_int == 6):
    print("Sunday")
