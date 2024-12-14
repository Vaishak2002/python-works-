class employee:

    id:int

    name:str

    age:int

    salary:int

    def set_employee(self,id,name,age,salary):

        self.id=id

        self.name=name                        #to initialize attributes of class employee

        self.age=age

        self.salary=salary

    def display(self):

        print(self.id,self.name,self.age,self.salary)

emp1=employee()   #object of class employee is created

emp2=employee()    #2nd object for another employee

emp1.set_employee(1,"xav",23,10000) #assigning values for 1st employee

emp2.set_employee(2,"vaishak",23,15000)

emp1.display()   #calling display method to display the details of emp1

