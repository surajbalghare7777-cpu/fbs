math=int(input("Enter marks in Math: "))
science=int(input("Enter marks in Science: "))
english=int(input("Enter marks in English: "))
social=int(input("Enter marks in Social: "))
hindi=int(input("Enter marks in Hindi: "))
avg=(math+science+english+social+hindi)/5
if avg>=90:
    print("distinction")
elif avg>=80:
    print("first class")
elif avg>=60:
    print("second class")
elif avg>=40:
    print("third class")
else:
    print("fail im sorry babu ghr jake sutti babu")