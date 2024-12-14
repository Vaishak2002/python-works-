class employee:

    id:int

    name:str

    age:int

    salary:int

    def __init__(self,id,name,age,salary): # " __init__ "is the "constructor" created

        self.id=id

        self.name=name                        #to initialize attributes of class employee

        self.age=age

        self.salary=salary

    def display(self):

        print(self.id,self.name,self.age,self.salary)

emp1=employee(1,"xav",23,15000)   #constructor is called whenever an object of the class is created

emp2=employee(2,"vaishak",23,25000)    


emp1.display()   #calling display method to display the details of emp1

emp2.display()
