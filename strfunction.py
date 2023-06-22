#withopout str
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = person("roshan", 22)
# print(p1)

#with str function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
      return f"{self.name},{self.age}"
p1=Person("age",30)  
print(p1)    
