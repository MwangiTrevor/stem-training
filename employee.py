class Employee (Person):
    def __init__(self,name,age,salary):
        super(),__init__(name,age)
        self.salary=salary
        p2=Employee("Trevor",1,500)
        p2.details()

