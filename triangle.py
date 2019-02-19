
# y=0
# x=
# mid=1
# height=5
# tri=True
# while tri:
    
#     if y<height:
#         print(
#         y=y+1
#     if y==height:
#         tri=False
#         print

# #x=5, y=3 box
# #--*--1
# #-***-3
# #*****5
# #x= y=
# #1----*----
# #3---***---
# #5--*****--
# #7-*******-
# #9*********
# # 
# # find correlation with bottom width and height

size = 2
while( size % 2 )==0:
    size=int(input("enter odd number: "))

y=0

while y < size/2:
    x = 0
    stars= 1 + (y * 2)
    spaces = size- stars
    while x < size:
        if spaces > 0:
            print(' ', end='')

            spaces = spaces-1

        elif stars > 0:
            print('* ', end='')

            stars = stars -1
        
        x=x+1
    print()

    y= y + 1