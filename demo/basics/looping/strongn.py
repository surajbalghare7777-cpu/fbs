n=int(input("enter the number"))
temp=n
sum=0
while temp>0:
    digit=temp%10

    temp//=10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum+=fact
if sum==n:
    print(f"{n} is a strong number")
else:
    print(f"{n} is not a strong number")