'''
Created on 29-Sept-2024
finally block is used for clean up activities
@author: Hp
'''
print(1+2)
print(3*5)
try:
    print(6/0)
except Exception as e:
    print(e)
finally:
    print("finally block")#for clean up activities it is in exception,there are other things also for clean up 
print(9^2)