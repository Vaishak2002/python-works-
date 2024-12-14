op=input("enter the operation")

def student_info(*args,**kwargs):

    if kwargs.get("operation")=="avg":

        return sum(args)/len(args)
     
    if kwargs.get("operation")=="total":

        return sum(args)

print(student_info(45,43,44,operation=op))