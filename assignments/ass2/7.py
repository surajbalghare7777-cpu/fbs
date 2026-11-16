num=int(input("Enter a number: "))
h=num//100
t=(num//10)%10
o=num%10
print(f'Hundreds: {h}, Tens: {t}, Ones: {o}')
sum=h+t+o
print(f'Sum of digits: {sum}')