class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def eat_drink(self):
        print("Eat chicken and drinke beer")

class Employee(Person):
    def __init__(self,name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal
    
    def work(self):
        print("coding python is very easy just link drinking chilled beer")

    def employee_info(self):
        print("Employee name:{}".format(self.name))
        print("Employee age:{}".format(self.age))
        print("Employee Number:{}".format(self.eno))
        print("Employee Salary:{}".format(self.esal))

e= Employee("Naveen", 27, "EMP101","10000")
e.eat_drink()
e.work()
e.employee_info()

#Single inheitance
class P:
    def m1(self):
        print("Parent method")
class C(P):
    def m2(self):
        print("Child method")
c= C()
c.m1()
c.m2()

#multi level inheritances

class P:
    def m1(self):
        print("Parent method")
class C(P):
    def m2(self):
        print("Child method")
class CC(C):
    def m3(self):
        print("sub child method")
c= CC()
c.m1()
c.m2()
c.m3()


#multiple inheritances
class P1:
    def m1(self):
        print("Parent1 Method")

class P2:
    def m2(self):
        print("Parent2 method")

class C(P1,P2):
    def m3(self):
        print("Child method")

c= C()
c.m1()
c.m2()
c.m3()

#Cyclic inheritance
#HYbrid inheritance
#Hyrarchical inheritance