class cars:

    def __init__(self,name,brand,fuel_type):

        self.name=name
        self.brand=brand
        self.fuel_type=fuel_type

    def display(self):

        print(self.name,self.brand,self.fuel_type)

    def __str__(self):      #string representing of an object using "__str__" method            

        return self.name
    
        return self.fuel_type
    
car1=cars("glanza","toyota","petrol")

print(car1)