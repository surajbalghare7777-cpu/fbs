###syntax
#1. if (condition):
    # code to execute if condition is true

#if condition is true, then the code block inside the if statement will be executed. 
#If the condition is false, the code block will be skipped.

#example
#n=int(input("Enter a number: "))
#if n>0:
 #   print("The number is positive.")

#2. if(condition):
        #statement
#   else:
        #statement
#if condition is true, then the code block inside the if statement will be executed. 
#If the condition is false, then the else block of code will be executed.

#example
#!num=int(input("Enter a number: "))
#if(num%2==0):
 #   print("The number is even.")
#else:
 #   print("the number is odd")#


#3.nested if else
#if(condition):
    #if():
        #statement
    #else
        #statement
#else:
    #if():
        #statement
    #else:
        #statement

#example
gender=str(input("Enter your gender (M/F): "))
age=int(input("Enter your age: "))
if gender=="M":
    if(age>=21):
        print("yes")
    else:
        print("sorry")
else:
    if(age>=18):
        print("yes")
    else:
        print("sorry")


#4.if else ladder

#example
n=int(input("enter a number"))
if(n==0):
    print("neutral")
elif(n>0):
    print("+ve")
else:
    print("-ve")
