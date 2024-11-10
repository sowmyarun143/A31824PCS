'''
Created on 29-Sept-2024
Exception Handling:Handling the errors that occur at runtime when the program is being executed
(Exception:unexpected one)
Types of Error:
1 Syntax Errors
2 Runtime Errors
    -network issues/server issues
    -Invalid inputs,End user input
    -program logic,etc...

Exception handling:
1 Try except
2 Try except except...
3 default except block
4 Group of exceptions 
@author: Hp
'''
from idlelib.idle_test.test_colorizer import tearDownModule
print(1+2)
print(3*5)
# try:
#     print(6/0)
# except ZeroDivisionError as ze:
#     print(ze)

"""try:
    print(6/'ptr')
except ZeroDivisionError as Ze:
    print(Ze)
except TypeError as Te:
    print(Te)"""
try:    
    try:
        print(6/0)
    # except:
    #     print("Exception error")#default exception
    except (ZeroDivisionError,TypeError) as e:
        print(6/'nour')#other exception occur within exception
except Exception as e:
    print(e)


print(9^2)