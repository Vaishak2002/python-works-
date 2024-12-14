num1=int(input("enter num1"))

num2=int(input("enter num2"))

try:
    result=num1/num2    #if error occured

    print(result)

except Exception as e :

    print(e)

    num2=int(input("enter num2"))

    result=num1/num2

    print(result)

print("file operations")

print("db commit")