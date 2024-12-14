from re import fullmatch

pan_card=input("enter the number:")

pattern="[A-Z]{3}[PZAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pan_card)

if matcher==None:

    print("invalid")

else:

    print("valid")