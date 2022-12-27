def matric():
    m = int(input("enter the rows"))
    n = int(input("enter the cols"))
    o = []
    for i in range(m):
        p = []
        for j in range(n):
            x = int(input("enter the elements"))
            p.append(x)
        o.append(p)

    return o


A = matric()
B = matric()
lst = []
for i in range(len(A[0])):
    for j in range(len(B[0])):
        sum = 0
        for k in range(len(A[0])):
            sum = sum + A[i][k] * B[k][j]
        lst.append(sum)
print(lst)