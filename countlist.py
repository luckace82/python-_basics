#without using list comprehension and count 
list=[1,2,2,3,2,3,4,40]
p=[]
u=[]
c=[]
list.sort()
for s in list:
    if s not in u:
        u.append(s) 
for j in u:
    count=0
    for s in list:
        if j==s:
            count+=1
    c.append(count)   
for i in range(len(u)):
    p.append(str(u[i])+":"+str(c[i]))
print(p)                
















# p=[]    
# i=[12,23,1,1,1,1,1]        
# j=[1,2,2,2,2,2,2,2]
# for x in range(len(j)):
#     p.append(i[x]:j[x])
# print(p)    