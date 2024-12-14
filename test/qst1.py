from re import finditer

f= open("test/qst1.txt")

count_alp=0

count_space=0

count_special=0

count_dig=0

content=f.read()

pattern="[a-zA-Z]"

matcher=finditer(pattern,content)

for i in matcher:

    count_alp+=1

print("count of alphabets",count_alp)

pattern2=" "

matcher2=finditer(pattern2,content)

for i in matcher2:

    count_space+=1

print("count of spaces",count_space)

pattern3="\s"

matcher3=finditer(pattern3,content)

for i in matcher3:

    count_special+=1

print("count of special char",count_special)

pattern4="[0-9]"

matcher4=finditer(pattern4,content)

for i in matcher4:

    count_dig+=1

print("count of digits",count_dig)


