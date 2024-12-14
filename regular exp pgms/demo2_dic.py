from re import finditer

text="I have 3 cars,2 bike and 1 -cycle"

matcher=finditer("[0-9]",text) # checks for 0 to 9 digits in the text given

# for obj in matcher:

    # print(obj.start(),obj.group())


# matcher2=finditer("[a-zA-z]",text) # checks for character small a to capital Z or " all alphabets]"

# for obj in matcher2:

#     print(obj.start(),obj.group())

# matcher3=finditer("[a-zA-z0-9]",text) # checks for  all alphanumerics

# for obj in matcher3:

#     print(obj.start(),obj.group())

# matcher4=finditer("[^ak]",text) #  to exclude a and k

# for obj in matcher4:

#     print(obj.start(),obj.group())

# matcher5=finditer("[^a-zA-Z0-9]",text) #  to check all special cahracters

# for obj in matcher5:

#     print(obj.start(),obj.group())

# " \w " represents alphanumerics

# matcher6=finditer("\w",text) #  to check alphanumerics use " \w "

# for obj in matcher6:

#     print(obj.start(),obj.group())

# matcher7=finditer("\d",text) #  to check digits use " \d "

# for obj in matcher7:

#     print(obj.start(),obj.group())

matcher8=finditer("\D",text) #  to "exclude" digits use " \D "

for obj in matcher8:

    print(obj.start(),obj.group())

    """"""

# " \W " can be used to check for " special characters " or " exclude alphanumerics "

# " \s " is used to check for spaces

#  " \S " used to exclude spaces

    """"""











