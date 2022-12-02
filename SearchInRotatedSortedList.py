lst=[5,6,1,2,3,4]
target=2
l=0
u=len(lst)-1
while(l<=u):
    mid=(l+u)//2
    if(lst[mid]==target):
        print(mid)
        exit(0)
    if(lst[l]<=lst[mid]):
        if(target>=lst[l] and target<lst[mid]):
            u=mid-1
        else:
            l=mid+1
    else:
        if(target>lst[mid] and target<=lst[u]):
            l=mid+1
        else:
            u=mid-1