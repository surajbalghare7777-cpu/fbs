#1.to make parameter optional
#2.Assign value to parameter in function definition 
#3.If we pass value to default parameter,it takes passed value
    #If we don't pass value to default parameter ,it take default value
#4.Flow from right to left

def emp(id,name='abc',sal=10000,dept='back office'):
    print('ID',id)
    print('NAME',name)
    print('SALARY',sal)
    print('DEPARTMENT',dept)
    print('#################################3')

emp(101,'ABC',500000,'IT')
emp(102)
emp(103,'DEF')
