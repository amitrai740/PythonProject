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