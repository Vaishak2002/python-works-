class Cusine:

    def __init__(self,cusine_name):

        self.cusine_name=cusine_name

    def display_cusine(self):

        print(self.cusine_name)

class Meal_type:

    def __init__(self,meal_type):

        self.meal_type=meal_type

    def display_meal_type(self):
        
        print(self.meal_type)

class dish(Cusine,Meal_type):

    def __init__(self, cusine_name,meal_type,dish_name):

        Cusine.__init__(self,cusine_name)

        Meal_type.__init__(self,meal_type)

        self.dish_name=dish_name

    def display_dish(self):

        self.display_cusine()

        self.display_meal_type()

        print(self.dish_name)

dish_instance=dish("chinese","dinner","dragon chicken")

dish_instance.display_dish()


        
        