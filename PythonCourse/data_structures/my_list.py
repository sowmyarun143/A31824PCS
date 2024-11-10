'''
Created on 16-Sept-2024
Lists:ordered,changeable,Duplicates allow
1.Creation:
    a Empty list
    b With Elements(List can be homogeneous / Heterogeneous)
    c using built-in function-List()
2. Accessing the List
    a Indexing
    b looping statements
    c Slicing Operator
@author: Hp
'''
'''
a = []# An Empty list can be  created
print(a)
print(type(a))

b = [1,2,3,4]#same data type(Homogeneous Data)
print(b)

c = [1,2.4,"Anu"]#Different data type(Heterogeneous Data)
print(c)

d = list(range(6))#List can be created using built-in function -list()
print(d)

#accessing using index
print(c[2])#using positive index
print(c[-2])#using negative index

#using looping statements

#(For loop)

print("For loop-iterates over the sequence:")
for index in c:
    print(index)
 
#(while loop)   
print("while loop")
print("lenght of c list:",len(c))
j=0
while j<len(c):
    print(c[j])
    j+=1
    
#list slicing 
#list[initial:end:Indexjump(step)]

e = list(range(2,21,2))#List can be created using built-in function -list()
print("e=",e)
"""print(e[0:4])#slicing
print(e[::])"""
e[5]=67#modification,replacing existing value
print(e)
e[5]=14#Duplicates allowed
print(e)

#Built-In functions to perform some operations
e.append(5)#extending the list by appending values at the end of list
print("e",e)

# e.clear()
# print("e",e)

x=e.copy()#copy list to another list
print(x)

print(e.count(14))#counts number 14 how many times exists in list

e.extend([6,7,8,9])#adding values at last of list different eements
print(e)

e.append([6,7,8,9])#adding as a last value completely as one value
print(e)

print(e[13])
print(e[15])

print(e.index(10))
print(e.index(8,2,16))
#print(e.index(8, -1, -10))

'''
'''
Q1 create a random list of numbers.Take an input from the user and determine
    a Whether that element present in the given list  
    b If present then display the count
    c Display the position/s at which the element is present
Q2 remove where ever taken elements which is present in the given list repeatedly 
'''
'''
e.insert(5,67)
print("e",e)
print(e.pop(5))
e.remove(14)
print("e",e)
print(e.pop())
e.reverse()

print("Reverse list=",e)
e.sort()#ascending order list
print("Ascending list:",e)
e.sort(reverse = True)#Descending order list
print("Descending list:",e)

#operators:
f=[1,2,3,4] 
print("e+f=",e+f)#extends of one list to another
#print("e*f=",e*f)#error:can't multiply sequence by non-int of type 'list'
print("f*2:",f*2)#extends of a list with the same list number of times specified

print(6 in e)#membership operators
print(18 not in e)
'''



#print(e.count(8))
#print(e.index(8,0,14))

'''
#Q1 solution
lst = [1,5,2,4,2,1,5,7,2,2,8,5,7,3,2,1,4,2]
print(lst)
posi_elems = []
elem = int(input("Enter an element which is to be check whether present in the list or not:"))
if elem  in lst:
    print("element is present in the given list")
    c = lst.count(elem)
    print("elements count present in this list:",c )
    i=0
    for i in range(len(lst)):
        if lst[i]==elem:
            posi_elems.append(i)
            i+=1
    print(posi_elems)  
       
else:
    print("element not present in the given list")
    
'''
#Q2 solution
lst = [1,5,2,4,2,1,5,7,2,2,8,5,7,3,2,1,4,2]
print(lst)
posi_elems = []
elem = int(input("Enter an element which is to be check whether present in the list or not:"))
if elem  in lst:
    print("element is present in the given list")
    c = lst.count(elem)
    print("elements count present in this list:",c )
    for i in range(len(lst)):
        if lst[i]==elem:
            posi_elems.append(i)
            i+=1
    print(posi_elems)  
  
    #print(len(lst))
    '''
    for j in lst:
        if j<=len(lst):
            a = lst.pop(j)
            print(a)
            
                
            print(lst)
       '''
    new_lst=lst.copy()
    
#    j=0
 #   for j in range(len(lst)):
#        if lst[j]!= elem:
#            new_lst.append(lst[j])
#        else:
#            lst.pop(j)
#        j=0
        
#    print(new_lst)

    for j in new_lst:#lst[:] copy list without effecting original list
        if j == elem:
            lst.remove(j)
                   
    print("After removing the user specified element from list,current list is:\n",lst)  
else:
    print("element not present in the given list")  
