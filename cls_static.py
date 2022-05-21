#If the value of a variable is not varied from object to object, such type of variables we have to
 #declare with in the class directly but outside of methods. Such type of variables are called Static
 #variables.

class Employee:
    #In general we can declare within the class directly but from out side of any method
    company = "caliper business solutions"
    def __init__(self):
        #Inside constructor by using class name
        Employee.company = "Infosys company"
    
    def m1(self):
        #Inside instance method by using class name
        Employee.company = "TATA company"
    
    #Inside classmethod by using either class name or cls variable
    @classmethod
    def m2(cls):
        cls.company = "Wipro company"
        Employee.company = "HCL Company"
    
    @staticmethod
    def m3():
        Employee.company = "BOSCH company"


#How to access the static variables
class Employee:
    company = "Caliper Business Solutions"
    def __init__(self):
        #inside constructor: by using either self or classname
        print(self.company)
        print(Employee.company)
    def m1(self):
        #inside instance method: by using either self or classname
        print(self.company)
        print(Employee.company)
    #inside class method: by using either cls variable or classname
    @classmethod
    def m2(cls):
        print(cls.company)
        print(Employee.company)
    
    #inside static method: by using classname
    def m3():
        print(Employee.company)

t1 = Employee()
#From outside of class: by using either object reference or classnmae
print(Employee.company)
print(t1.company)


#Local variable
# Sometimes to meet temporary requirements of programmer,we can declare variables inside a method directly,such type of variables are called local variable or temporary variables.

class Employee:
    def m1(self):
        company_income = 1000
        print(company_income)
    

