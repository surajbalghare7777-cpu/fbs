n=int(input("enter the number"))
temp=n
armstrong=0
while temp>0:
    digit=temp%10
    armstrong+=digit**3
    temp//=10

if armstrong == n:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")