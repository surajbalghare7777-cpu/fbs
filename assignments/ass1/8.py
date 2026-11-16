days=int(input('enter number of days:'))
years=days//365 #floor division://
r=days%365 #mod:%
months=r//30
rm=r%30     
w=r//7
rr=r%7
print(f'years={years},months={months},weeks={w},days={rr}')
