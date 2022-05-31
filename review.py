class Person :
    def __init__(self,name,age):
      self.name=name
      self.age=age
    def details(self):
        print(f"my name is {self.name} and i am {self.age}")
p1=Person("Trevor",18)
p1.details()

class Employee(Person):
    def __init__(self,name,age,salary):
        super(),__init__(name,age)
        self.salary=salary
    def details(self):
      print(f"my name is{self.name.salary}and i an{self.age}")
p2=Employee("Trevor",18,500)
p2.details()
