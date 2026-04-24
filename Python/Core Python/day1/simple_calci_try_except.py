try:
    num1=int(input('enter first number: '))
    num2=int(input('enter 2nd number: '))
    print('1.Add','\n2.Sub','\n3.Mul','\n4.Div')
    ask=input('Choose Operation')
    if ask=='1':
        print('Sum is',num1+num2)
    elif ask=='2':
        print('Sub is',num1-num2)
    elif ask=='3':
        print('Mul is',num1*num2)
    elif ask=='4':
        if num2==0:
            print('Cannot Divide by Zero')
        else:    
            print('Div is',num1/num2)
    else:
        print('Choose a Valid Operation')
except ValueError:
    print('Invalid number')