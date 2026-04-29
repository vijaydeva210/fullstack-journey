num=int(input('enter a number: '))
bkp=num
rev=0
while num>0:
    r=num%10
    rev=rev*10+r
    num=num//10
if rev==bkp:
    print('Palindrome')
else:
    print('Not Palindrome')