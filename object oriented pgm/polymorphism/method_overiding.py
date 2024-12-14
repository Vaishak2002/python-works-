class parent:

    def mobile(self):

        print("nokia3100")

class child(parent):

    def mobile(self):
        
        print("iPhone")

child_instance=child()

child_instance.mobile()