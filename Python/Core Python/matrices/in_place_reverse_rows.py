l=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rows=len(l)
columns=len(l[0])
n=columns-1
for i in range(rows):
    for j in range(columns):
        if i==j:
            break
        l[i][n-j],l[i][j]=l[i][j],l[i][n-j]
print(l)