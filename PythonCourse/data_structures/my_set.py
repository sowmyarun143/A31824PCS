'''
Created on 16-Sept-2024
Set: A set is a collection which is unordered, unchangeable*, and unindexed.
    *sets are unchangeable but can remove items and add new items
    
Creation:
    1.Empty set(need to use empty set() built-in method )
    2.With immutable items separated by comma within curly braces{}
    3.using built-in set() method
Accessing:
    1 Using looping statements
    
@author: Hp
'''


a = {}# create empty dictionary 
print(a)
print(type(a))


fruit = {"apple","banana","mango"}#unordered set
print(fruit)
print(type(fruit))

fruit = {"apple","banana","mango","apple"}#duplicates not allowed
print(fruit)

fruit = {"apple","banana","mango",True,1,2}#True and 1 considered same value in set also False and 0
print(fruit)

fruit = {"apple","banana","mango",False,0,1,2}
print(fruit)

fruit = {"apple","banana","mango"}#unordered set
print(fruit)
print(len(fruit))#length of set fruit

fruit =set(("apple", "banana", "mango",None))#set() built-in function
print(fruit)

#accessing: For loop
print("For loop statement:")
fruit = {"apple","banana","mango"}
for i in fruit:
    print(i)

#membership operators
fruit = {"apple","banana","mango"}
print("apple" in fruit)

fruit = {"apple","banana","mango"}
print("cherry"  not in fruit)

'''
cannot change set elements once created but can add or remove items to set
methods:
'''
#Add using add()

fruit = {"apple","banana","mango"}
fruit.add("Cheery")
print(fruit)

#add items from another set into the current set, use the update() method.
fruit = {"apple","banana","mango"}
otherfruit = {"cheery","papaya","pineapple"}
fruit.update(otherfruit)
print(fruit)

#update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)
fruit = {"apple","banana","mango"}
mylist = ["cherry","kiwi"]
fruit.update(mylist)
print(fruit)

#remove(): If the item to remove does not exist, remove() will raise an error.
fruit = {"apple","banana","mango"}
fruit.remove("mango")
print(fruit)

#clear():removes all the elements from the set
"""fruit = {"apple","banana","mango"}
fruit.clear()
print(fruit)
"""

#discard:If the item to remove does not exist, discard() will not  raise any error.
fruit = {"apple","banana","mango"}
fruit.discard("cherry")
print(fruit)

#pop():Removes an element from the set
print("pop() gives:")
fruit = {"apple","banana","mango"}
x=fruit.pop()
print(x)

#del :delete entire set
'''
fruit = {"apple","banana","mango"}
del fruit
print(fruit)##this will raise an error because the set no longer exists
print(fruit)
'''

#copy():copy a set
fruit = {"apple","banana","mango"}
x = fruit.copy()
print("X=",x)

#Difference(-):Return a new set that will contain only the items from the first set(a) that are not present in the other set(b)
a = {1,2,3,4,5}
b = {6,7,8,9,1}
c = a.difference(b)
#a - b
print("Difference of a and b set in set c:",c)

#Difference_update(-=):keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
a = {1,2,3,4,5}
b = {6,7,8,9,1}
a.difference_update(b)
#a -= b
print("Difference update of a and b set:",a)

#Intersection(&):Returns a set that contains the similarity between two or more sets.
a = {1,2,3,4,5}
b = {3,8,4,7,1}
#c = a.intersection(b)
c = a & b
print("Intersection of a and b:",c)
print("set a:",a)

#Intersection_update(&=):Removes the item which is not present in both the sets
'''
a = {1,2,3,4,5}
b = {3,8,4,7,1}
c = a.intersection_update(b)
print("Intersection update of a and b:",c)
'''#results None
a = {1,2,3,4,5}
b = {3,8,4,7,1}
#a.intersection_update(b)#removes 2 and 5 in set a
a &= b
print("Intersection update of a and b(set a):",a)

#isdisjoint():Returns whether two sets have a intersection(False) or not(True)
a = {1,2,3,4,5}
b = {13,8,9,7,6}
c = a.isdisjoint(b)
print(c)

#Union(|):Return a set that contains all items from both sets, duplicates are excluded
a = {1,2,3,4,5}
b = {3,8,4,7,1}
#c=a.union(b)
c = a | b
print("Union:",c)

#update(|=):updates the current set, by adding items from another set
a = {1,2,3,4,5}
b = {3,8,4,7,1}
#a.update(b)
a |= b
print("update:",a)

#issubset(<= and <):returns True if all items in the set exists in the specified set, otherwise it returns False.
a = {1,2,4}
b = {3,1,6,2}
#c = a.issubset(b)
#c = a <= b
c = a  < b 
print("a and b sets are subsets?=",c)

#issuperset(>= and >):returns True if all items in the specified set exists in the original set, otherwise it returns False.
a = {1,2,3,4,5,6,7}
#b = {4,3,7}
b = {4,3,8}
#c = a.issuperset(b)
#c = a >= b
c = a > b
print("a and b are supersets?=",c)

#symmetric_difference(^):Return a set that contains all items from both sets, except items that are present in both set
a = {1,2,3,4,5}
b = {7,1,9,3,6}
c= a.symmetric_difference(b)
print("symmetric difference:",c)


#symmetric_difference_update(^=):Remove the items that are present in both sets, AND insert the items that is not present in both sets but it will change the original set instead of returning a new set.
a = {1,2,3,4,5}
#b = {4,1,6,2,7}
b = {6,7,8,9}
a.symmetric_difference_update(b)
print("Symmetric_difference_update :",a)

