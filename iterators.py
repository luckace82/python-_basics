class person:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
p1=person()
myiter=iter(p1)    
print(next(myiter))
print(next(myiter))
print(next(myiter))