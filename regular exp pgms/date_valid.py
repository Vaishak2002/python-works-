from re import fullmatch

month=input("enter the month:")

pattern="([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])"

matcher=fullmatch(pattern,month)

if matcher==None:

    print("invalid")

else:

    print("valid")