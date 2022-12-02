def binary(lst,n):
    m=len(lst)
    l=0
    u=m-1

    while(l<=u):
        mid=(l+u)//2
        if(lst[mid]==n):
            print("found at position",mid)
            exit(0)
        else:
            if lst[mid]>n:
                u=mid-1
            else:
                l=mid+1
    print("elemet not found")












lst=[10,20,30,40,50,60,70]
n=500
binary(lst,n)
a=5
b=0
try:
    print(a/b)
    k = int(input("enter a number"))
    print(k)

except ZeroDivisionError as e:
   print(e,'error')

except ValueError:
    print("Invalid error")
except Exception as e:
    print(e)