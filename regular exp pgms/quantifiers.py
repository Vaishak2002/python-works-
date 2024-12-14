from re import finditer

text="abbbababbabaaaab"

# pattern="a{2}"  #a is repeted for 2 times

# matcher1=finditer(pattern,text)

# for obj in matcher1:

#     print(obj.start(),obj.group())



pattern="a{1,3}" # check for " one a " and " 3 a's "

matcher2=finditer(pattern,text)

for obj in matcher2:

    print(obj.start(),obj.group())

