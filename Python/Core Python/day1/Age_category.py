name=input('Enter your name: ')
age=int(input('enter your age: '))

if age<18:
    print('Mr/Mrs',name,'You are minor')
elif 18<age<60:
    print('Mr/Mrs',name,'You are major')
elif age>60:
    print('Mr/Mrs',name,'You are Senior')
else:
    print('Enter a valid age')