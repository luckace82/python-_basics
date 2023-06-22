# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# x=[f"{a}:{sample_list.count(a)}" for a in set(sample_list)]
# print(x)    
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
thisdict={}
for i in set(sample_list):
    thisdict.update({i :sample_list.count(i)})
print(thisdict)    
