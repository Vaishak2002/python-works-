text1="PQRST"
text2="ABC"

#output=PAQBRCST

len1=len(text1)

len2=len(text2)

new=""

for i in range(0,len2):

    new+=text1[i]+text2[i]

for j in range(len2,len1):

    new+=text1[j]

print(new)