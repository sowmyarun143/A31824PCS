'''
Created on 28-Sept-2024
abstraction:Something which exists in idea/thought but not implemented

Types of methods
1. Implemented methods:method definition and method body
2. unimplemented methods:method definition with pass keyword
An object can't be created from an abstract class, unless abstract method is implemented by its subclass

Abstract class conditions:
1. one or more unimplemented methods
2. an object can't be created from an abstract class

Interface:It is a class having all abstract methods
@author: Hp
'''
from abc import *
class HumanBeings(ABC):
    def __init__(self,name,legs=2,hands=2):#init constructor#*self takes values as object/instance once created object
        self.name = name
        self.legs = legs
        self.hands = hands
        print(f"object with name {self.name} having {self.legs} legs and {self.hands} hands")
    @abstractmethod
    def walk(self):#unimplemented method
        pass
    def run(self):#implemented method
        print(f"{self.name} running")

class Male(HumanBeings):
    def walk(self):
        print(f"{self.name} is walking")
    def boxing(self):
        print(f"{self.name} is boxing")
obj1 = Male("Vivek")
obj1.run()
obj1.boxing()
obj1.walk()