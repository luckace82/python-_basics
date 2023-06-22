set1 = list({10, 20, 30, 40, 50})
set2 = list({30, 40, 50, 60, 70})
l=[j  for i in set1 for j in set2 if i==j]       
print(set(l))     