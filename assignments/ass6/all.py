def ass1():
    for i in range(1,7):
        for j in range(1,7):
            if(i==1 or i==6 or j==1 or j==6):
                print("*", end="")
            else:
                print(" ", end="")

        print()

def ass2():
    n=4
    num=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(num,end=" ")
            num+=1
        print()

def ass3():
    for i in range(4):
        print(" " * (3 - i), end="")
        c = 1
        for j in range(i + 1):
            print(c, end=" ")
            c = c * (i - j) // (j + 1)
        print()


def ass4():
    for i in range(5):
        for j in range(i + 1):
            print(chr(65 + j), end=" ")
        print()

def ass5():
    for i in range(1,6):
        for j in range(1,6-i):
            print(" ",end="")
        for j in range(1,i+i):
            print("*",end="")
        print()

def ass6():
    for i in range(1,6):
        for j in range(1,6-i):
            print(" ",end=" ")
        for j in range(1,i+i):
            print(j,end=" ")
        print()


def ass7():
    for i in range(1,6):
        for j in range(1,6-i):
            print(" ",end=" ")
        for j in range(1,i+i):
            print(chr(64 + j),end=" ")
        print()

ass7()