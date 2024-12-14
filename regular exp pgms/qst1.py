# starting with a alphabet p-t
# in second place must be a number that is divicible by 3
# folowed by any number, alpabet , @

from re import fullmatch

user_input=input("enter the text")


pattern="[p-tP-T][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("invalid")

else:

    print("valid")