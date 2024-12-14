class shipping:

    def claculate_weight(self,weight):

        print(weight*5)

class express_shipping(shipping):

    def calculate_weight(self,weight):

        print(weight*20)

class standard_shipping(express_shipping):

    def calculate_weight(self, weight):
        
        print(weight*10)

std_instance=standard_shipping()

exp=express_shipping()

ship=shipping()

std_instance.calculate_weight(10)

exp.calculate_weight(10)

ship.claculate_weight(10)