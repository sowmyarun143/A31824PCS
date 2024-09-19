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
'''
d = {}
print(type(d))
'''
d = {1:"vivek",2:"sowmya",3:"meghana"} #ordered
print(d)

d = {1:"vivek",2:"sowmya",3:"meghana","a":"sowmya"} 
print(d)

d = {1:"vivek",2:"sowmya",3:"meghana",1:"abc"} #duplicates not allowed,values overwrite
print(d)
print(len(d))

print(d[1])#display 1st element

#dictionary changeable
d[4] = "sanvi"#add element
print(d)

#del d[4]#delete particular element
#print(d)

"""d.clear()#clear all elements
print(d)"""
