from re import finditer

text="fatcatrunveryfasttocaththerat"

pattern="at"

#to find the pattern>>

matcher=finditer(pattern,text) #[(start,group),()]

for obj in matcher:

    print(obj.start(),obj.group())