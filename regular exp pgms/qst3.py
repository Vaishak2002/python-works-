# starting with KL

#folloed by 2 digits

#alphabet min 1 and max 2 
#followed by 4 digits

from re import fullmatch

u_input=input(" enter the text")

pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,u_input)

if matcher==None:

    print("invalid")

else:

    print("valid")
