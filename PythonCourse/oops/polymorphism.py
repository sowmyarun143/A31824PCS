'''
Created on 28-Sept-2024
polymorphism: many forms
Types of polymorphism:
1.Overloading(CompileTime)
    a.operator overloading- *,+
    b.method overloading
    c.constructor overloading
2.Overriding(Runtime)
    a.method overriding
    b.construction overriding
@author: Hp
'''
from pip._vendor.pygments.unistring import No
class HumanBeings:
    def __init__(self,name=None,legs=2,hands=2):#constructor overloading with variable parameters
        self.name = name
        self.legs = legs
        self.hands = hands
        print("This is constructor overloading")
        print(f"object with name {self.name} having {self.legs} legs and {self.hands} hands")
    def walk(self):
        print(f"{self.name} walking")
    def run(self):
        print(f"{self.name} running")
    
    
obj1 = HumanBeings("sowmya")
def add(a=0,b=0):#formal arguments#method overloading
    print(f"sum of {a} and {b} is",a+b)
    
add(3, 4)  
#Method overriding occurs when a method in a subclass has the same name, 
#parameters, and signature as a method in its parent class
#constructor overriding example in  inheritance module