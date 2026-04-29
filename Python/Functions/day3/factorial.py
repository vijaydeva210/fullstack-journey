def factorial(num):
    fact=1
    for i in range(num,0,-1):
        fact=fact*i
    return fact
print(factorial(2))
print(factorial(4))