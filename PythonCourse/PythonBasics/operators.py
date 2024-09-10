'''
Created on 04-Sept-2024

@author: Hp
"operation is process operating operands by an operator" in general
operator:
It is symbol which is applied on operands to perform some specific actions/tasks/operation
Types of operators:
'''
a = 56
b = 5
#assignment operators
#arithmetic operations : +,-,*,/,**,//
print(a%b)
print(a/b)
print(2**3)
print(a//b)

#relational(comparision) operators: <,>,==,!=,>=,<=
print(a>b)
print(a<b)
print(a==b)
print(a!=b)

#logical operators:and,or,not

print("And:")
print(True and True)#and
print(True and False)#and
print(False and True)#and
print(False and False)#and

print("Or:")
print(True or True)#or
print(True or False)#or
print(False or True)#or
print(False or False)#or

print("Not:")
print(not True)#not
print(not False)#not

#membership operators: in,not in
print("membersship operator:")
print("s" in "sowmya")
print("s" not in "sowmya")
print("S" in "sowmya")#case sensitive


#identity operator:is,is not
#e =[1,2,3]#list
#f = [1,2,3]
e =5
f =5
print("identity operator:")
print(e is f)
print(e is not f)
print(e == f)#cheching the values in comparision operators
print(id(e))#checking the location
print(id(f))#checking the location

#bitwise operators:&,|,^,~,<<,>>
print("bitwise operator:")
print(bin(5))
print(5<<1)#left shit
print(5>>1)#right shift

c = 7
d = 4
print(c & d)
print(c | d)
print(c ^ d)
print(~c)
