'''
Created on 28-Sept-2024
Types of variables:
1. Instance variable/object variable
2. Local/method variables:limited inside method only:scope remains until object exists
3. Static /class variables:Inside the class along with class name can use
@author: Hp
'''
class Student:
    school = "iQuest"#static variables/class variables
    def __init__(self,name,roll_no):#instance variables
        self.name = name
        self.roll_no = roll_no
    
    def total_marks(self,kan,eng,hind):#local variables
        print(f"Total marks of {self.name} from {Student.school} is:",kan+eng+hind)
        
    # def get_individual_marks(self):
    #     print(kan,eng,hind)#local variables inside another method not allow 
    #it is just example to show local variables cannot access from other methods

std1 = Student("Sowmya",1)
std1.total_marks(100, 89, 78)       