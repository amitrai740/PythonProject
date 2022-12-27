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
target = 1
i = 0
j = len(A[0]) - 1
while (i <= len(A) - 1 and j >= 0):
    if (A[i][j] == target):
        print(i, j)
        exit()
    elif (target > A[i][j]):
        i = i + 1
    else:
        j = j - 1
print("not found")