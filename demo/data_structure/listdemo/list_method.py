li=[40,10,40,30,20]
#li.append(50) 1method
#li.clear() 2method

#deepcopy and shallow copy -nested list
####DEEPCOPY creates a new outer object and recursively copies the nested objects. 
#Changes to nested objects in the copy do not affect the original.
####SHALLOW COPY creates a new outer object, but the nested objects inside it are still shared with the original object.
#li=[40,10,40,30,20,[90,100]]
#li2=li.copy() 3method
#li[5][0]=70
#print(li)
#print(li2)

#print(li.count(40)) 4method
print(li.extend([70,80])) #5method
print(li.index(20)) #6method show the index for the returned valued
print(li.insert(1,60)) #7method insert the value on the returned indexed and right shifts the remaining value
print(li.pop(4)) #8method removed the value for the returned index
print(li.remove(40)) #9method removed the value directly w/o seeing the index
print(li.reverse()) #10method reverse the list
print(li.sort()) #11method sorts the list in ascending order
print(li.sort(reverse=True)) #12method sorts the list in descending order
print(li)