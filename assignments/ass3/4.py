a1=int(input("enter angle 1: "))
a2=int(input("enter angle 2: "))
a3=int(input("enter angle 3: "))
if (a1+a2>a3) and (a2+a3>a1) and (a1+a3>a2):
    print("Triangle is valid")
else:
    print("Triangle is not valid")