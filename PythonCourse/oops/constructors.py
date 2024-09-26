'''
Created on 22-Sept-2024
Constructors:methods used to construct/initialize the object
1. It is not mandatory to define a constructor by users
2. Constructors is called implicitly at the time object creation.But, 
   Constructors can also called explicitly as required just like other methods
3. Constructors can create without parameters
@author: Hp
'''
class HumanBeings:
    def __init__(self,name):#init constructor#*self takes values as object/instance once created object
        self.name = name
        print("This is constructor")
    def walk(self):
        print(f"{self.name} walking")
    def run(self):
        print(f"{self.name} running")

obj1 = HumanBeings("sowmya")#object creation,constructors called implicitly here
obj1.__init__("sowmya")#can call constructor explicitly also like other methods 
obj1.run()
obj1.walk()
print(obj1.name)

obj2 = HumanBeings("meghana")
obj2.run()
obj2.walk()
print(obj2.name)
print(dir(obj1))
