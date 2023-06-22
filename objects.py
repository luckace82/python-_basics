total=0
class bill:
    def __init__(self,item,rate,number):
        self.item=item
        self.rate=rate
        self.number=number
    def myfunc(self):
        print("the total price of "+self.item +" is ",self.rate*self.number)
item=[bill("mouse",100,3),bill("keyboard",1900,3)]
for i in item:
    i.myfunc()
for i in item:
    total=total+i.rate*i.number    
print("The amount you need to pay is ",total)    