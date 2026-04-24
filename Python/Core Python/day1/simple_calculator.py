while True:
    print('1.Sum','\n2.Sub','\n3.Mul','\n4.Div','\n5.Exit')
    ask=input('choose any option: ')
    if ask=='5':
        print('You are exiited from calculator')
        break
    num1=int(input('enter 1st number: '))
    num2=int(input('enter 2nd number: '))

   
    if ask=='1':
        print(num1+num2)
    elif ask=='2':
        print(num1-num2)
    elif ask=='3':
        print(num1*num2)
    elif ask=='4':
        print(num1/num2)

    else:
        print('choose correct option')