# ---------- Prime Number ----------
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# ---------- Palindrome Number ----------
def is_palindrome_number(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    return original == reverse


# ---------- Perfect Number ----------
def is_perfect(n):
    if n <= 1:
        return False
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total == n


# ---------- Strong Number ----------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def is_strong(n):
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        total += factorial(digit)
        n = n // 10
    return total == original


# ---------- Armstrong Number (without exponent operator) ----------
def power(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

def is_armstrong(n):
    original = n
    num_digits = count_digits(n)
    total = 0
    while n > 0:
        digit = n % 10
        total += power(digit, num_digits)
        n = n // 10
    return total == original


# ---------- Fibonacci Series ----------
def fibonacci(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


# ---------- Menu ----------
def main():
    while True:
        print("\n--- MENU ---")
        print("1. Check Prime Number")
        print("2. Check Palindrome Number")
        print("3. Check Perfect Number")
        print("4. Check Strong Number")
        print("5. Check Armstrong Number")
        print("6. Print Fibonacci Series")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            num = int(input("Enter a number: "))
            print(num, "is prime" if is_prime(num) else "is not prime")

        elif choice == "2":
            num = int(input("Enter a number: "))
            print(num, "is a palindrome" if is_palindrome_number(num) else "is not a palindrome")

        elif choice == "3":
            num = int(input("Enter a number: "))
            print(num, "is a perfect number" if is_perfect(num) else "is not a perfect number")

        elif choice == "4":
            num = int(input("Enter a number: "))
            print(num, "is a strong number" if is_strong(num) else "is not a strong number")

        elif choice == "5":
            num = int(input("Enter a number: "))
            print(num, "is an Armstrong number" if is_armstrong(num) else "is not an Armstrong number")

        elif choice == "6":
            terms = int(input("Enter number of terms: "))
            print("Fibonacci series:", *fibonacci(terms))

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()