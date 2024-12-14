op=input("enter the operation")

def sort_num(*args,**kwargs):

    if kwargs.get("reverse")=="True":

        return sorted(args,reverse=True)
    
    if kwargs.get("reverse")=="False":

        return sorted(args,reverse=False)
    
print(sort_num(1,2,3,4,5,6,7,8,9,reverse=op))
        

