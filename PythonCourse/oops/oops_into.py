'''
Created on 22-Sept-2024
class :a blueprint or mould for create an object
object: It is a variable which has its properties and its methods

main pillors of oops:
1 Inheritance
2 Polymorphism
3 Abstraction
4 Encapsulation

@author: Hp
'''
class HumanBeings:
    def walk(self):
        print("i am walking")
    def run(self):
        print("i am running")

obj1 = HumanBeings()
print(type(obj1))
obj1.run()
obj1.walk()