def largest(a,b,c):
    if a>=b and a>=c:
        return f'largest is {a}'
    elif b>=a and b>=c:
        return f'largest is {b}'
    else:
        return f'largest is {c}'
print(largest(1,2,3))
print(largest(3,2,1))
print(largest(2,3,1))