def palindrome(num):
    try:
        num=abs(num)
        bkp=num
        rev=0
        while num>0:
            r=num%10
            rev=rev*10+r
            num//=10
        if rev==bkp:
            return'Palindrome'
        else:
            return'Not Palindrome'
    except ValueError:
        return 'Enter valid data'
print(palindrome(1223))
print(palindrome(121))
print(palindrome(123))
