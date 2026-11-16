def addition():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a + b  ##return passes the value outside of the function or it jumps out of the function and the static frame is deallocated
result = addition()
print("The sum is:", result)





####without passing parameter
####with returning value