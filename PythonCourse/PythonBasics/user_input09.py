'''
Created on 09-Sept-2024

@author: Hp
input from keyboard
input() takes string as input only.
type casting need to do for to take another datatype
conversion of one dat type to another data type
'''
# a = input("enter a number")#input() only takes string 
# b = input("enter second number")
# c = a + b
# print(c)

a = float( input("enter a number:"))#type casting to float data type
b = float(input("enter second number:"))
c = a + b
#print(c)
#print("addition of two numbers:"+c)#only concatinate str to str
print("addition of two numbers a and b:",+c)

print(f"addition of two numbers {a} and {b}:",c)#formatted strings
print("addition of two numbers",a,"and",b,":",c)#normal way 
print("addtion of two numbers %f and %f is %f" %(a,b,c))#just like c, but complex

