l=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rows=len(l)
columns=len(l[0])
for i in range(rows):
    for j in range(columns):
        print(l[j][i],end=' ')
    print()