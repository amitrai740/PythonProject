def insertion(lst):
    l=len(lst)
    for i in range(1,l):
        temp=lst[i]
        j=i-1
        while(j>=0 and lst[j]>temp):
           lst[j+1]=lst[j]
           j=j-1
        lst[j+1]=temp

    print(lst)



lst=[10,20,1,5,1,7,1]
insertion(lst)
