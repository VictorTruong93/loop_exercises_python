


service =input("Please enter bill level of service (bad, fair, good) ")

if service == "bad":
    tip=0.10
elif service == "fair":
    tip=0.15
elif service == "good":
    tip=0.2
else: 
    print("Please enter exactly bad, fair, good ")
    
bill =int(input("Please enter bill amount. $"))
people =int(input("Please enter amount of people splitting bill after tip: "))
tip_total =int(bill*tip)
bill_total = int(bill+tip_total)
bill_split = round(float(bill_total/people),2)
print("Tip Amount: $"+ str(tip_total))
print("Total Amount: $"+str(bill_total))
print("Amount per person: $"+str(bill_split))