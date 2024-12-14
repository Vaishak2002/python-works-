class animal:

    def __init__(self,name,species):

        self.name=name
        self.species=species

    def __str__(self):
        
        return self.name
    
class lion(animal):

    def __init__(self, name, species):
        super().__init__(name, species)

    def sound(self):

        print("ror")

lion_instance=lion("lion","cat")

lion_instance.sound()

print(lion_instance)
        