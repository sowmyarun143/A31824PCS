'''
Created on 10-Sept-2024

@author: Hp
looping statements: these statements helps us to execute statements repeatedly.
    1.Initialization,2.condition check,3.Increment/Decrement
types:
    1.while loop
    2.for loop
    3.nested loop

Looping control statements:
    1.Break
    2.Continue
'''
#1.while loop:
"""count = 0 #initialization
while(count<5):#condition check
    #count=count+1#increment
    count+=1#another way to increment
    print("Hello world!")"""

#2.For loop:
# for count in range(0,10,2):#range(start,end,stepping) to print even numbers
#     print(count)
#     print("Hello World!")
    
#looping control statements example:
#break statement:
'''
while True:
    print("Hello world!")
    check = input("Do you want to continue?(y/n)")
    if check=="n":
        break
        
a=0
while a<=100:
    print(a)
    a+=1
    if a==51:
        break

for i in range(100):
    print(i)
    if i==50:
        break
'''

#continue statement:
'''
for i in range(100):
    if i == 50:
        continue #skips 50 and continue to print remaining
    print(i)
'''   

a=0
while a<=100:
    if a==50:
        a+=1
        continue
    print(a)
    a+=1
    
   
    
    