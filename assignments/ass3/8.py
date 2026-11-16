gender=str(input("Enter your gender (M/F): "))
age=int(input("Enter your age: "))
if gender=="Male" and age>=21:
    print("You are eligible for marriage")
elif gender=="Female" and age>=18:
    print("You are eligible for marriage")
else:
    print("You are not eligible for marriage")