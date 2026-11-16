n=5


def pattern_a(n):
    k = 1                                   # gap between the two stars
    for i in range(1, n + 1):               # upper half
        for j in range(1, n - i + 1):
            print(" ", end=" ")
        print("*", end=" ")
        if i > 1:
            for j in range(1, k + 1):
                print(" ", end=" ")
            print("*", end=" ")
            k += 2
        print()
    k = 2 * n - 3
    for i in range(n, 0, -1):               # lower half
        for j in range(1, n - i + 1):
            print(" ", end=" ")
        print("*", end=" ")
        if i > 1:
            for j in range(1, k + 1):
                print(" ", end=" ")
            print("*", end=" ")
            k -= 2
        print()
   



def pattern_b(n):
    print("##############################")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
  




def pattern_c(n):
    print("##############################")
    for i in range(1, n + 1):
        if i == n:
            for j in range(1, n + 1):
                print(j, end=" ")
        else:
            print(1, end=" ")
            if i > 1:
                for j in range(2, i):
                    print(" ", end=" ")
                print(i, end=" ")
        print()




def pattern_d(n):
    print("##############################")
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):       # leading spaces
            print(" ", end=" ")
        for j in range(i, 2 * i):           # i ... 2i-1
            print(j, end=" ")
        for j in range(2 * i - 2, i - 1, -1):   # 2i-2 ... i
            print(j, end=" ")
        print()



def pattern_e(n):
    print("##############################")
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):       # leading spaces
            print(end=" ")
        if i == n:
            for j in range(1, n + 1):
                print(j, end=" ")
        else:
            print(1, end=" ")
            if i > 1:
                for j in range(2, i):
                    print(" ", end=" ")
                print(i, end=" ")
        print()



def pattern_f(n):
    print("##############################")
    for i in range(1, n + 1):
        if i == 1:
            for j in range(1, n + 1):
                print(j, end=" ")
        else:
            print(i, end=" ")
            for j in range(1, n - i):       # gap between the two columns
                print(" ", end=" ")
            if i < n:
                print(n, end=" ")
        print()



def pattern_g(n):
    print("##############################")
    for i in range(1, n + 1): 
        for j in range(1, n - i + 1):       # leading spaces
            print(" ", end=" ")
        for j in range(1, i + 1):           # 1 ... i
            print(j, end=" ")
        for j in range(i - 1, 0, -1):       # i-1 ... 1
            print(j, end=" ")
        print()


def pattern_h(n):
    print("##############################")
    k = 2 * n - 3                           # gap in the middle
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(1, k + 1):
            print(" ", end=" ")
        k -= 2
        for j in range(i, 0, -1):
            if i != n or j != n:            # last row shares the middle number
                print(j, end=" ")
        print()


pattern_a(n)
pattern_b(n)
pattern_c(n)
pattern_d(n)
pattern_e(n)
pattern_f(n)
pattern_g(n)
pattern_h(n)