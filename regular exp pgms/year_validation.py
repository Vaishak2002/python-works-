from re import fullmatch

pattern= "((18|19)[0-9]{2}|20[01][0-9]|202[0-4])"

year= input("enter the year")

matcher=fullmatch(pattern,year)

print("invalid" if matcher==None else "valid")