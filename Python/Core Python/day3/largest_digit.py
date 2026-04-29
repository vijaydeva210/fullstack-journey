try:
    num=int(input('Enter a number: '))
    num=abs(num)
    if num==0:
        print(0)
    else:
        l=0
        while num>0:
            r=num%10
            if r>l:
                l=r
            num//=10
        print(l)
except ValueError:
    print('Enter a valid number')