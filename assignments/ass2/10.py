n=int(input("enter a three digit number"))
h=n//100
t=(n//10)%10
o=n%10
r=o*100+t*10+h
print("reversed number is:",r)