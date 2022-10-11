a=10
b=20
m=max(a,b)
for i in range(m,a*b+1,m):
    if i%a==0 and i%b==0:
        print(i)
        break