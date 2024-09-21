'''
Created on 19-Sept-2024
Dictionary:stored data values in keys and values
syntax:
d = {key1:value1,key2:value2,...}
1 creation:
    a empty dictionary
@author: Hp
'''
#a. empty dictionary
from optparse import Values
'''
d = {}#empty dictionary
print(type(d))
'''
d = {1:"vivek",2:"sowmya",3:"meghana"} #ordered
print(d)

d = {1:"vivek",2:"sowmya",3:"meghana","a":"sowmya"} 
print(d)

d = {1:"vivek",2:"sowmya",3:"meghana",1:"abc"} #duplicates not allowed,values overwrite
print(d)
print(len(d))#length of dictionary

print(d[1])#display 1st element

#dictionary changeable
d[4] = "sanvi"#add element
print("Dictionary after adding element:",d)

#del d[4]#delete particular element
#print(d)

"""d.clear()#clear all elements
print(d)"""

e = d.fromkeys([1,2,3,4], "Null")
print("fromkeys function:",e)

print("items:",d.items())
print("values:",d.values())
print("keys:",d.keys())

print(d.get(3))
print(d.pop(2))#any value can remove here
print(d)#print after pop

print(d.popitem())#remove last item with completely with key and value






