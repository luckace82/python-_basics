class vehicle:
    def __init__(self,max_speed,mileage,price):
        self.max_speed=max_speed
        self.mileage=mileage
        self.price=price
    def myfunc(self):
        print("max speed :",self.max_speed,"mileage:",self.mileage,"price:",self.price)    
item=[vehicle(100,20,200000),vehicle(150,15,300000)]
for i in item:
    i.myfunc()