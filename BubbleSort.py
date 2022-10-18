def bubble(lst):
    l=len(lst)
    for i in range(l-1):
        for j in range(l-1-i):
            if(lst[j]>lst[j+1]):
                lst[j],lst[j+1]=lst[j+1],lst[j]


    print(lst)








lst=[2,5,8,1,99,100,45,66]
bubble(lst)