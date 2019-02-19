# y=0
# x=5
# grid=True
# while grid:
    
#     if y<6:
#         print('*'*x)
#         y=y+1
#     if y==5:
#         grid=False
width = int(input("width?: "))
height = int(input("height?; "))
y=0

while y<height:
    # during while y<height, x = 0 to reset x <width loop
    x = 0
    while x<width:
        # end='' makes print command stop on same line, python does not enter to new line
        print("*", end='')
        x += 1
    # print() makes python jump down 1 line.
    print()
    y+=1

# this is loop within loop to draw x variable before increasing y 