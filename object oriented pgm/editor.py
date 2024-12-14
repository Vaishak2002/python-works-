class editor:

    def __init__(self,name,vendor):

        self.name=name
        self.vendor=vendor

    
    
    def __str__(self):
        
        return self.name
    

editor1=editor("xav","revons")

editor2=editor("zod","revons")

print(editor1,editor2)