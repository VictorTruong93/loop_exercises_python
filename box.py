box_height=2
length=int(input("Box Length: "))
user_height=int(input("Box Height: "))

print(length*'*')
while box_height<user_height:
    
    
    if box_height<user_height:
        print("*"+(' '*(length-2))+"*") 
        box_height+=1
    else:
        break
        
        
print("*"*length)
        