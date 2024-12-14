from re import fullmatch

pattern="[a-z]+[0-9]*[a-z]*[0-9]*@gmail.com" #" + " indicates there must be atleast one 

gmail=input("enter the gmail id")

matcher=fullmatch(pattern,gmail)

print("invalid" if matcher==None else "valid")