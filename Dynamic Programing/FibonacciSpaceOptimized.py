def fibonacci(n):
    a = 0
    b = 1

    if n<0:
        print("Enter Positive Number")
    elif n == 0:
        return a
    elif n == 1:
        return n
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(10))