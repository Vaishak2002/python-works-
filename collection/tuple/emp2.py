employee={"id":10,"name": "xav","dept":"cse","age":23,"salary":25000}

# using .get(key) method

# print(employee.get("dept"))  # if invalid key, it returns none

# # pop(key)  to remove

# employee.pop("salary")

# print(employee)

# # return all the keys ==> keys() method

# for k in employee.keys():

#     print(k)

# # fetch all values ==> values() method

# for v in employee.values():

#     print(v)

# fetch keys and values ==> items()

for k,v in employee.items():

    print(k,v)





