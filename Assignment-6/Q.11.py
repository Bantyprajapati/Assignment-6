month=int(input("Enter month: "))
if month in (1,2,3,5,7,8,10,12):
    print("31 Days")
elif month in (4,6,9,11):
    print("30 Days")
elif month==2:
    print("28 or 29 Days")
else:
    print("invalid month number")
    
