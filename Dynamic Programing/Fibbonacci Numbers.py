""" Dynamic Progrming with Memoization """

FibArray = [0,1]

def  fibonacci(n):
    if n<0:
        print('Incorrect Number')
    elif n<= 2:
        return 1
    else :
        temp_fib = fibonacci(n-1) + fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib 
n = 10
print(fibonacci(n))

