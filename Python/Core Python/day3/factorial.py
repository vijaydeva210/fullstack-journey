try:
    num=int(input('enter a number: '))
    fact=1
    if num==0:
        print(fact)
    elif num<0:
        print('Negative numbers are not allowed')
    else:
        for i in range(num,0,-1):
            fact=fact*i
        print(fact)
except ValueError:
    print('Enter a valid number')