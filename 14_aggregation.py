
# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Department:
    def __init__(self,employee):
        self.employee=employee


class Employee:
    def __init__(self,name):
        self.name= name


emp = Employee("ALI")
dept = Department(emp)

print(dept.employee.name)