def factorial(n):#defining a function factorial
    if n<0:
        return "Sorry, factorial does not exist for negative numbers."
    elif n==0 or n==1: #base case 
        return 1
    else:
        return n*factorial(n-1) #recrusive code
num=int(input())
print(f"The factorial of {num} is {factorial(num)}")
