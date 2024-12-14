class animals:

    sound:str

    name:str

    def set_animal(self,name,sound):

        self.name=name

        self.sound=sound

    def display(self):

        print("sound of",self.name ,"is",self.sound)

lion_instance=animals()

cat_instance=animals()

lion_instance.set_animal("lion","roar")

cat_instance.set_animal("cat","meow")

lion_instance.display()

cat_instance.display()