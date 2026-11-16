p=int(input("Enter the principal amount: "))
r=int(input("Enter the rate of interest: "))
t=int(input("Enter the time period: "))
a=p*(1+r/100)**t
print("The compound interest is:", a-p)