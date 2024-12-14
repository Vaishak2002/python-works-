class Person:

    def __init__(self,age,name):

        self.name=name
        self.age=age

    def display_person(self):

        print(self.name,self.age)

class Employee:

    def __init__(self,emp_id,salary):

        self.emp_id=emp_id
        self.salary=salary

    def display_employee(self):

        print(self.emp_id,self.salary)

class Manager(Employee,Person):

    def __init__(self,age,name, emp_id, salary,department):

        Person.__init__(self,age,name)

        Employee.__init__(self,emp_id,salary)

        self.department=department

    def display_manager_info(self):

        self.display_person()

        self.display_employee()

        print(self.department)

manger_instance=Manager(23,"XAVIER",1001,50000,"hr")

manger_instance.display_manager_info()
        
    