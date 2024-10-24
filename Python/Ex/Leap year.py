year=int(input("enter the year : "))
if(year % 400 == 0) and (year % 100 == 0):
    print("Leap year !!!")
else:
    print("Not a Leap year")