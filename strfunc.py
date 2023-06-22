class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"    
p1=person("lakesh",4)
p2=person("lak",1)
print(p1)
print(p2)        
