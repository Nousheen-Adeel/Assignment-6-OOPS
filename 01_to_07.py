# #1. Using self

# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        return f' Name is: {self.name} \n Marks are: {self.marks}'

s1: Student = Student("Nousheen", 98) 
s2:Student = Student('Farah',86)
print(s1.display())
print("**** Student details****")
print(s1.name)
print(s1.marks)
print(s2.name)
print(s2.marks)

# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count= 0
    def __init__(self):
        Counter.count +=1


    @classmethod
    def display_count(cls):
        return f'objects created {cls.count}'
    
obj1:Counter = Counter()
obj2:Counter = Counter()
print (Counter.display_count())


# 3. Public Variables and Methods

# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        return f'{self.brand} is starting..'

car: Car = Car('Toyota')
print (car.brand)
print(car.start())

# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "ABC bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1: Bank = Bank()
b2: Bank= Bank()   
print(b1.bank_name)
print(b2.bank_name)
Bank.change_bank_name("XYZ Bank")
print(b1.bank_name)

print("**********************************************************")
print("5. Static Variables and Static Methods")

# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    def add(a,b):
        return a+b
print("MathUtils")
print(MathUtils.add(2,5))

print("**********************************")
print("6. Constructors and Destructors")
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).""")

class Logger:
    def __init__(self):
        print("Logger object is created" )
    #def __del__(self):
        #print("Logger object Deleted")
    
log:Logger = Logger()
print(log)

print("****************************")
print("7.Access Modifiers: Public, Private, and Protected")

# Assignment:
# Create a class Employee with:

#     a public variable name,

#     a protected variable _salary, and

#     a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name,salary,ssn):
        self.name=name
        self._salary= salary
        self.__ssn= ssn

emp1: Employee= Employee("Nousheen", 500000, "123-456-789")
print(emp1.name)
print(emp1._salary)
#print(emp1.__ssn)

print("we can do it through name mandling")
print(emp1._Employee__ssn)

