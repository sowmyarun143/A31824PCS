'''
Created on 21-Sept-2024

@author: Hp
'''
'''
a = 5
b = 6
c = a+b
print(f"sum of {a} and {b} is ",a+b)
'''
def display():#functions without parameters
    print("welcome to iQuest")
def add(a,b):#functions with parameters
    #print("Addition of two numbers")
    #print(f"sum of {a} and {b} is ",a+b)
    return a+b
def mul(a,b):
    #print(f"multiplication of {a} and {b} is",a*b)
    return a*b

display()
#total = add(7,6)  
#print(f"total:",total)
print("Sum of two numbers:",add(7,6)) 
print("mul of two numbers:",mul(7,6))
#mul(total, 8)

def add_mul(a,b):
    c = add(a, b)#calling a function from another function
    d = mul(a, b)  
    #return c,d
    return add(a,b),mul(a, b)#also return functions itself

#x,y=add_mul(6,7)    
#print("add:",x)
#print("mul:",y)
print(f"addition,multiplication of two numbers:",add_mul(6, 7))