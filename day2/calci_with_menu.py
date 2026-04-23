while True:
    try:
        print('1.Add','\n2.Sub','\n3.Mul','\n4.Div','\n5.Power','\n6.Percentage','\n7.Exit')
        ask=input('Choose any operation: ')
        if ask=='7':
            print('Calci is closed')
            break  
        if ask not in ['1','2','3','4','5','6']:
            print('Invalid option')     
        num1=int(input('enter 1st number: '))
        num2=int(input('enter 2nd number: '))
        if ask=='1':
            print('Sum is',num1+num2)
        elif ask=='2':
            print('Sub is',num1-num2)
        elif ask=='3':
            print('Mul is',num1*num2)
        elif ask=='4':
            if num2==0:
                print('A number cannot devide by Zero')
            else:
                print('Div is',num1/num2)

        elif ask=='5':
            print(f'{num1}**{num2} is',num1**num2)
        elif ask=='6':
            if num2==0:
                print('Cannot calculate percentage')
            else:
                print(f'{num1}%{num2} is',(num1/num2)*100)
    except ValueError:
        print('Enter valid numbers')