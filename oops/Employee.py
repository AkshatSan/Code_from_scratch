class Employee:
    def __init__(self,role,dep,salary):
        self.role=role
        self.dep=dep
        self.salary=salary
    def showDetails(self):
        print("The details are")
        print("ROle",self.role)
        print("dep",self.dep)
        print("salary",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Analyst","DATA science","50")
engg1=Engineer("AKSHAT","24")
print(engg1.showDetails())