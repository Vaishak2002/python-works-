from re import fullmatch #check for exact match

user_iput=input("enter the variable name")

pattern="[a-zA-z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,user_iput) # fullmatch() returs "None" is false

if matcher==None:

    print("invalid")

else:

    print("valid")


