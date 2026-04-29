def reversedd(num):
        num=abs(num)
        rev=0
        while num>0:
            r=num%10
            rev=rev*10+r
            num//=10
        return rev
print(reversedd(341))
print(reversedd(1234))
print(reversedd(4321))
print(reversedd(an))