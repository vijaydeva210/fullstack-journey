def reverse(num):
    try:
        num=abs(num)
        rev=0
        while num>0:
            r=num%10
            rev=rev*10+r
            num//=10
        return rev
    except ValueError:
        print('Enter a valid number')
print(reverse(341))
print(reverse(1234))
print(reverse(4321))