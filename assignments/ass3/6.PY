cp=int(input("Enter the cost price: "))
sp=int(input("Enter the selling price: "))
if sp>cp:
    print("Profit")
elif sp<cp:
    print("Loss")
else:
    print("No Profit, No Loss")