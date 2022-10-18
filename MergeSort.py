
def merge(list):
    if len(list)>1:
        mid = len(list) // 2
        left_list = list[:mid]
        right_list = list[mid:]
        merge(left_list)
        merge(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list[k]=left_list[i]
                i+=1
                k+=1
            else:
                list[k]=right_list[j]
                j+=1
                k+=1
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1





num=int(input("enter the number of list"))
list1=[int(input()) for x in range(num)]
merge(list1)
print(list1)
