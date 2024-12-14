employee={"eid":1,"name":"sura","salary":25000,"dept":"CSE","exp": 6 }

# print(employee)

employee["contact"]=1234567890

# print(employee)


if employee["exp"]>5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000

# print(employee)

if employee["exp"]>5:

    employee["role"]="sde"

else:

    employee["role"]="jde"

print(employee)