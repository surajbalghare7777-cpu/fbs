data=[1,2,3,4,5,6,7,8,9,10]

r=list(filter(lambda n:n%2==0,data))###typecasting to list
print(r)

r1=list(filter(lambda n:n*n,data))###typecasting to list(it consider the number which is not equal to zero,null,none or blank)
print(r1)