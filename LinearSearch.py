def Linear(lst,n):
    for i in range(len(lst)-1):
        if(lst[i]==n):
            print("found at position",i)
            exit(0)
    print("not found")








lst=[10,20,30,40,50,60,70]
n=100
Linear(lst,n)