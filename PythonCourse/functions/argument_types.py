'''
Created on 21-Sept-2024
Types of arguments:
1.positional arguments
2.keyword arguments
3.variable-length arguments
4.variable-length keyword arguments
@author: Hp
'''
'''
from functions.my_functions import *#import all functions by * from my_functions here
from data_structures.my_set import mylist
#def add(a,b):#formal arguments
#    print(f"sum of {a} and {b} is",a+b)

add(7, 8)#actual arguments,positional arguments
add(b=7,a=8)#keyword arguments

def addition(*a):#variable-length arguments
    print(a)
    
addition()
addition(5,6)
addition(5,6,7)

#Q1 In a given tuple,Add all the elements and give the output
#don't use built in function 'sum'

def details(**x):#variable-length keyword arguments
    print(x)
    
details(id=1,name="sowmya",place="mysore",job="tester")
'''
#Q1 solution: 
#a.without using functions


ttl = 0
mytpl=(3,4,6,7,9,2)
for i in mytpl:
    ttl=ttl+i

# print("Sum of given tuple elements are:",ttl)

# def addtpl(mytpl):#using function with parameters
#         ttl = 0
#         for i in mytpl:
#             ttl=ttl+i 
#         print("Sum of given tuple elements are:",ttl)
# mytpl=(3,4,6,7,9,2)        
# addtpl(mytpl)

def addtpl(*mytpl):#using variable-length argument
        ttl = 0
        for i in mytpl:
            ttl=ttl+i 
        return ttl

a=addtpl(3,4,6,7,9,2)
print("Sum of given tuple elements are:",a)