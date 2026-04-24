try:
    name=input('Please enter your name: ')
    age=int(input('Enter your age: '))
    salary=int(input('Enter your salary: '))
    if age>18 and salary>20000:
        print('Mr/Mrs',name,'You are eligible')
    elif age<0 or salary<0:
        print('youve entered negative Data')
    else:
        print('Mr/Mrs',name,'You are not eligible')
except ValueError:
    print('Please enter Valid Data')