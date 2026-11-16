#1. structure 
li=[10,20,30,40,3.14,'abc']

#2.type of data:heterogeneous

#3.sequential:Ordered

#4.changeable:mutable 

#5.duplication:allowed

print(id(li))
li[0]=90
print(id(li))
print(type(li))
print(li)

###### list can have heterogeneous data(multiple type of data can be stored)
##### list is in ordered way it(data's sequence cant be changed automatically)
##### we can do changes in list(can also change the order of list)
##### duplication is allowed in list(same data could be stored) 