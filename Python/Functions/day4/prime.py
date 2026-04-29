def prime(n):
    if n<=1:
        return 'Not Prime'
    else:

        for i in range(2,n//2+1):
            if n%i==0:
                return 'Not Prime'
        return 'Prime'
print(prime(1))
print(prime(2))
print(prime(9))
print(prime(11))