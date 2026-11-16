sub1=int(input('enter the marks of maths:'))
sub2=int(input('enter the marks of science:'))
sub3=int(input('enter the marks of english:'))
sub4=int(input('enter the marks of social:'))
sub5=int(input('enter the marks of hindi:'))
total=sub1+sub2+sub3+sub4+sub5
print('the total marks obtained is:', total)
avg=total/5
print('the average marks obtained is:', avg)
if avg>=90:
    print('grade is A')
elif avg>=80:
    print('grade is B')
else:
    print('grade is C')
    