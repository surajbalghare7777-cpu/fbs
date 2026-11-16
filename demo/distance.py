p=input("enter the path in 4 forms EWNS=  ")
x=0
y=0
for i in p:
    if i=="N":
        y+=1
    elif i=="S":
        y-=1
    elif i=="E":
        x+=1
    elif i=="W":
        x-=1
    else:
        print("invalid input")
        break
else:
    print("final co-ordinates are ",x,y)
    d=((x**2)+(y**2))**0.5
    print("distance from origin is ",d)
