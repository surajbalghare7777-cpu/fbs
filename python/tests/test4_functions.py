# Q1: factors of a number
def factors(num):
    print("Factors of", num, ":", ", ".join(str(i) for i in range(1, num + 1) if num % i == 0))

# Q2: factorial using recursion
def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)

# Q3: "Z" pattern
def z_pattern(n):
    print("*" * n)
    for i in range(n - 2):
        print(" " * (n - 2 - i) + "*")
    print("*" * n)

factors(int(input("Enter number: ")))
print("Factorial =", fact(int(input("Enter number for factorial: "))))
z_pattern(int(input("Pattern width: ")))
