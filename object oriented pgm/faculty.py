class faculty:

    name:str

    age:int

    experience:int

    course:str

    def set_faculty(self,name,age,experience,course):

        self.name=name

        self.age=age

        self.experience=experience

        self.course=course

    def display(self):

        print(self.name,self.age,self.experience,self.course)

faculty1=faculty()

faculty1.set_faculty("xav",23,3,"btech")

faculty1.display()

