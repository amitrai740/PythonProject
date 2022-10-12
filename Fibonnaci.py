def fibonnaci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)


m=int(input("enter the no of series you want to print"))
for i in range(m):
    print(fibonnaci(i))