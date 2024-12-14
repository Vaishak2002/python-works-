
class parent:

    def vehicle(self):

        print("parent class attributes accesed from child class")

class child(parent):   #inheritance syntax-->child inherits from parent class

    pass

child_instance=child()

child_instance.vehicle()  #child class accesses "vehicle()" method from parent class

