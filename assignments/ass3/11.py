ticket=int(input("Enter the ticket price: "))
pp=int(input("enter number people you want:"))
for i in range(pp):
    age=int(input("Enter the age of person: "))
    if age<=12:
        print("discount of 30%",ticket-(ticket*0.3))
    elif age>=60:
        print("discount of 50%",ticket-(ticket*0.5))
    else:
        print("no discount",ticket)
