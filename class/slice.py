text=" dohairas ambaadi"

n_word=text[0:9]

print(n_word)

print(text[10:18])

print(text[::-1]) #string reverse

text1="alan@gmail.com"

print(text1.index("@"))

print(text1[0:text1.index("@")])


#

text2="hellopython"

o_index=text.index("o")

rev=text2[o_index::-1]

balance_str=text2[o_index::]

word=rev+balance_str

print(word)

#merge 2 strings

text3="PQRST"

text4="ABC"

#output=PAQBRCST