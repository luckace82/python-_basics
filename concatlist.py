a=["hello ","take "]
b=["sir","mam"]
newlist=[i + j for i in a for j in b ]#using list comprehension

print(newlist)
#i runs from first to last of a
#j traverse from first to last of b
#two lists are given
a=["hello ","take "]
b=["sir","mam"]
c=[]#an emty list is introduced
for i in a:#i traverses from the first element to last of first list
    for j in b:#j traverses from the first element to last of second list
        #loop is nested
        newlist=i+j  
        c.append(newlist)#result are displayed in list as newlist is not in list form
print(c)    #printing th final list
# step 1: start
# step 2: initialize two different given list and one empty list new
# step 3: initialize variable i and j as the contents of list 1 and list 2 respectively
# step 4: using an outer for loop iterate through the items of list
#          i.e ,for i in list 1
# step 5: similarly use inner for loop & iterate through the items of list 2
#          i.e , for j in ist 2
# step 6: add the two items of different list and assign it to new
#          i.e, new=i+j
# step 7: print new