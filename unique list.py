def unique_list(list1):
    list=[x for i,x in (list1) if x not in list1[:i] ]
    return list
print(unique_list([1,2,3,4,1,2,3,4,5,3,2,2,2,2,2,2]))