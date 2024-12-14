
class superhero:

    name:str

    suit:str

    def __init__(self,name,suit):

        self.name=name
        self.suit=name

    def __str__(self):
        
        return self.name
    
class spiderman(superhero):

    def __init__(self, name, suit):
        
        super().__init__(name, suit)

    def superpower(self):

        print("strong","webs")

    
spiderman_inst=spiderman("spiderman","spidersuit")

spiderman_inst.superpower()

print(spiderman_inst)
        