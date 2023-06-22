import itertools
keys = ['Ten', 'Twenty', 'Thirty','aaa','a']
values = [10, 20, 30]
x=dict(itertools.zip_longest(keys,values,fillvalue="none"))
print(x)  