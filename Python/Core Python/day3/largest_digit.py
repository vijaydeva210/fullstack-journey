try:
    num=int(input('Enter a number: '))
    num=abs(num)
    l=float('-inf')
    if num==0:
        print(0)
    else:
        while num>0:
            r=num%10
            if l<=r:
                l=r
            num//=10
        print(l)
except ValueError:
    print('Enter a valid number')