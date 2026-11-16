f=int(input("enter feet"))
i=int(input("enter inches"))
t_i=f*12+i
print("total inches:",t_i)
t_cm=t_i*2.54
print("total centimeters:",t_cm)
t_m=t_cm/100
print("total meters:",t_m)