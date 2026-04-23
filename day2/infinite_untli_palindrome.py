while True:
    try:
        num=int(input('enter a number: '))
        num=abs(num)
        bkp=num
        rev=0
        while num>0:
            r=num%10
            rev=rev*10+r
            num=num//10
        if rev==bkp:
            print('Palindrome')
            break
        else:
            print('Not Palindrome')
    except ValueError:
        print('Enter a valid input')