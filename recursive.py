def sum(num):
    if num==0:
        return 0
    else :
        return num+sum(num-1)
print("the sum is",sum(10)) 
