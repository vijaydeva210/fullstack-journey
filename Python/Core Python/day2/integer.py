try:
    num=int(input('enter a number: '))
    if num>0:
        print('Positive')
    elif num<0:
        print('Negative')
    else:
        print('Zero')
except ValueError:
    print('Enter a valid number')
    

