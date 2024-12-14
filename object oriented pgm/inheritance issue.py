class Grandparent:

    def m(self):

        print("grand parent method m1")

class Parent:

    def m(self):

        print("parent method m2")

class Child(Grandparent,Parent): #here grandparent class is inherited first
    def m3(self):

        print("child method m3")

child_instance=Child()

child_instance.m() #here method "m()" of class grandparent is called, cuz grandparent class is inherited at first than parent's

child_instance.m3()


