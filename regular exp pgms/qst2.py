#rule 10 digit
#validate mobile number
# with or without country code 91 at the starting

from re import fullmatch

u_input=input("enter the ph no")

pattern="(91)?[0-9]{10}"

matcher=fullmatch(pattern,u_input)

if matcher==None:

    print("invalid")

else:

    print("valid")