a1=int(input("enter angle 1: "))
a2=int(input("enter angle 2: "))
a3=int(input("enter angle 3: "))
if a1==a2==a3:
    print("Triangle is Equilateral")
elif a1==a2 or a2==a3 or a1==a3:
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")