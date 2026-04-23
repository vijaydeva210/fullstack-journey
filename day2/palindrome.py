char=input('enter a number or word: ')
if char==char[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')