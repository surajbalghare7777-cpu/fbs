amount=int(input("Enter amount in rupees: "))
l=[500,200,100,50,20,10,5,2,1]
count=amount//l
if count>0:
    print(f"{count} notes of {l}")
    amount=amount%l
