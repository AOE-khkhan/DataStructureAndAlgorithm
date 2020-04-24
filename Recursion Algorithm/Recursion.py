# Recursion is process of defining something in terms of itself

def factorial(x):
    ''' Recursive function to find the factorial of an integer '''
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))
num =5
print(f'The factorial of {num} is {factorial(num)}')
# Output: The factorial of 5 is 120