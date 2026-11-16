cost=int(input("Enter cost of item: "))
discount=int(input("Enter discount percentage: "))
discount_amount=(cost*discount)/100
sp=cost-discount_amount
print("Discount amount: ",discount_amount)