#using list comprehension and set

a=[1,2,2,1,1,1,1,2,3,3,4]
list=[x for x in set(a)]
cou=[a.count(j) for j in a]
p=[f"{list[i]}:{cou[i]}" for i in range(len(set(a)))]
print(p)  

