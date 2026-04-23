num=int(input('enter a number: '))
reverse=0
while num>0:
    r=num%10
    reverse=reverse*10+r
    num=num//10
print(reverse)