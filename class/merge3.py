text1="PQRST"
text2="ABC"

#output=PAQBRCST

len1=len(text1)

len2=len(text2)

smallest=len1 if len1<len2 else len2

largest_text= text1 if len(text1)>len(text2) else text2


new=""

for i in range(0,smallest):

    new+=text1[i]+text2[i]

balance=""

balance+=largest_text[smallest:]

new+=balance

print(new)