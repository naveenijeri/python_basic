#if the value of the variable is varied from object to object is called instance variable
#Delare instance variable inside constructor, inside instance method, outside of the class.
#inside constructor
class Employee:
    def __init__(self):
        self.name = "Naveen"
        self.enumber = "EMP101"
        self.salary ="35000"
e = Employee()
print(e.__dict__)

#inside instance method
class Employee:
    def __init__(self):
        self.name = "Naveen"
        self.enumber = "EMP101"
        self.salary ="35000"
    
    def assign_deptment(self):
        self.department = "Operation"

e = Employee()
e.assign_deptment()
print(e.__dict__)


#outside of the class 

class Employee:
    def __init__(self):
        self.name = "Naveen"
        self.enumber = "EMP101"
        self.salary ="35000"
    
    def assign_deptment(self):
        self.department = "Operation"

e = Employee()
e.assign_deptment()
e.address= "586201,Wandal,Vijayapur district."
print(e.__dict__)

# We can access instance variables with in the class by using self variable and outside of the class by
class Employee:
    def __init__(self):
        self.name = "Naveen"
        self.enumber = "EMP101"
        self.salary ="35000"

    def display(self):
        print(self.name)
        print(self.enumber)
e = Employee()
e.display()
print(e.enumber,e.name)

# delete the instance varibale 
class Employee:
    def __init__(self):
        self.name = "Naveen"
        self.enumber = "EMP101"
        self.salary ="35000"
    
    def delete_name(self):
        del self.name
e = Employee()
print("instance variables",e.__dict__)
e.delete_name()
print("after deleteing instance method",e.__dict__)
del e.salary
print("after deleting outside of the calss", e.__dict__)

#note : objects which are deleted from one object will not be deleted from another object.



