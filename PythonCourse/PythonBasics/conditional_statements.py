'''
Created on 09-Sept-2024

@author: Hp
conditional statement:
1 If statement
2 If-Else statement
3 Series If-else statement(If-elif-else statement))
4 Nested If-else statement
    
'''

age = int(input("Please enter your age:"))
"""
#1.If-else statement:

if age >= 18:
    print("Allow inside")
else: 
    print("Don't allow")
"""
'''
#2.if-elif-else statement:
if age < 0:
    print("Age doesn't allow negetaive so,Enter proper age")
elif age <=18 and age>12:
    print("Belongs to Teenager group")
elif age>=60:
    print("belongs to Senior citizens group")
elif age<=12:
    print("Belongs to children group")
else:
    print("Belongs to Adult group")

''' 
#3.nested If-else statement:

if age<0:
    print("Age doesn't allow negative so,Enter proper age")
else:
    if age>18:
        if age >=60:
            print("Belongs to Senior Citizens group")
        else:
            print("Belongs to Adult group")
    else:
        if age<=12:
            print("Belongs to children group")
        else:
            print("Belongs to Teenage group")

