#1.to reduce the line code
#2.perform same task on multiple time on different inputs

def sq(n):
    return n*n

data=[1,2,3,4,5,6,7,8,9,10]

##############method 1
result=list(map(sq,data))###typecasting to list
print(result)

###############method 2
result=list(map(lambda n:n*n*n,data))###typecasting to list
print(result)