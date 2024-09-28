'''
Created on 28-Sept-2024
Encapsulation:Restricting the access of data members(variables,methods)
Types /levels of encapsulation:
1 Protected members:
  -Can't be accessed outside the class but,
   can be accessed within the same class and its subclasses
   -we use single underscore '_' as prefix for any data members
2 private members:
  -can accessed within a class
  - we use double underscore '__' as prefix for any data members
@author: Hp
'''
class HumanBeings:
    def __init__(self,name,legs=2,hands=2):#init constructor#*self takes values as object/instance once created object
        self.name = name
        self._legs = legs
        self.__hands = hands
        print(f"object with name {self.name} having {self._legs} legs and {self.__hands} hands")
    def __walk(self):
        print(f"{self.name} walking")
    def _run(self):
        print(f"{self.name} running")

obj1 = HumanBeings("sowmya")
obj1._run()
obj1._HumanBeings__walk()#name mangling when private members
