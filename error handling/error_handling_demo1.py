num1=int(input("enter num1"))

num2=int(input("enter num2"))

try:
    result=num1/num2    #if error occured

    print(result)

except Exception as e:

    print("error occured") 
    
    print(e)                             #message after error occured

print("file write")

print("database commit")