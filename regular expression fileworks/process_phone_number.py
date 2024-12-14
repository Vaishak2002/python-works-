from re import fullmatch

f=open("/Users/vaishakj/Desktop/pythonworks/regular expression fileworks/ph_nos.txt","r")

for line in f:

    phone=line.rstrip("\n")

    pattern="(91)?[0-9]{10}"

    matcher=fullmatch(pattern,phone)

    if matcher!=None:

        print(phone)