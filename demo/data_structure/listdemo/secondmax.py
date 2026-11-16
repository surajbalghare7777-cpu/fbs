l=[12, 35, 1, 10,200, 34, 1]

max=l[0]
smax=0

for i in range(1,len(l)):
    if l[i]>max:
        smax=max
        max=l[i]
    elif l[i]>smax:
        smax=l[i]

print("First and Second maximum element in the list is:", max,"and", smax)