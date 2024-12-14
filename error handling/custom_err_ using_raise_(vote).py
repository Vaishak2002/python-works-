def vote(age):

    if age<18:

        raise Exception("invalid age")
    
    else:

        print("voted")

age=int(input("enter the age"))

try:

    vote(age)

except Exception as e:

    print(e)

print("hello")

print("hai")