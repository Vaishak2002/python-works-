class Grandparent:

    def m1(self):

        print("grand parent method m1")

class Parent:

    def m2(self):

        print("parent method m2")

class Child(Grandparent,Parent): #multiple inheritance -->child class inherits directly from both parent and grandparent classes 

    def m3(self):

        print("child method m3")

child_instance=Child()

child_instance.m1()
child_instance.m2()
child_instance.m3()