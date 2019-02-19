day = int(input("What to do today? Please enter 0-6 "))

if day==0 or day==6:
    print("sleep in")
elif (day<6) and (day>0):
    print("go to work")
else:
    print("Please select from 0-6")
