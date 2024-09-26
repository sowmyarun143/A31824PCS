'''
Created on 26-Sept-2024
Inheritance: Inherits the properties and behavior of one class (super class / parents class) into another class(derived class/child class)
super class / parents class: class from which properties and behavior inherited  
sub class/child class : class which inherits the properties and behavior

Types of inheritance:
1 Single level Inheritance
2 Multi level Inheritance
3 Multiple Inheritance

*Method Resolution order

@author: Hp
'''
class GrandFather():
    def __init__(self,name,age):
        print("This is GF Constructor",name,age)
        
    def gf_method(self):
        print("This is grand father method")
        
class Father(GrandFather):# single Inherited here
    def __init__(self,name,age):
        print("Father Constructor")
        super().__init__(name,age)
    def f_method(self):
        print("This is father method")
    def car(self):
        print("Fathers car") 

class Mother():
    def m_method(self):
        print("This is mother method")
    def car(self):
        print("Mothers car")       
            
class Child(Father,Mother):#multi level before adding mother,#multiple heritance after adding mother
    def __init__(self,name,age):
        print("Child Constructor")
        super().__init__(name,age)
    def c_method(self):
        print("This is child Method")

        
obj1 = GrandFather("ajja",78)
obj1.gf_method()

obj2 = Father("Appa",52)    
obj2.f_method()
obj2.gf_method()

obj3 = Child("Son",28)
obj3.c_method()
obj3.f_method()
obj3.gf_method()#multi level
obj3.m_method()#multiple inheritance
obj3.car()#follow method resolution order

print("Method resolution order:")
print(Child.mro())
