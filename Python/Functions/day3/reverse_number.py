def reversedd(num):
    try:
        if num.isdigit()==True:
            num=abs(num)
        rev=0
        while num>0:
            r=num%10
            rev=rev*10+r
            num//=10
        return rev
    except ValueError:
        return'Enter a valid number'
print(reversedd(341))
print(reversedd(1234))
print(reversedd(4321))
print(reversedd(an))