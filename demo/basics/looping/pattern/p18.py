for i in range(1,6):
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(1,7-i):
    for j in range(6-i,0,-1):
        print("*",end=" ")
    print()