#go it from gogle

a = [1,2,2,1,1,1,1,2,3,3,4]
p = [f"{x}:{a.count(x)}" for x in set(a)]
print(p)
