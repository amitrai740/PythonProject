a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
m=max(a,b)
for i in range(m,a*b+1,m):
    if i%a==0 and i%b==0:
        print(i)
        break