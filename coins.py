# define variables first(below)

coin_bag=0
collector=True
while collector:
   
    print("You have "+str(coin_bag)+" coins.")
    user=input("Do you want a coin? (yes or no) ")
    
    if user =="yes":
          coin_bag=coin_bag+1

    elif user=="no":
        print("bye")
        collector=False