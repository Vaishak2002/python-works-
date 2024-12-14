text=input("enter the text")

length=len(text)-1

reversed=""

for i in range(length,-1,-1):

    reversed+=text[i]

print("is palindrome" if text==reversed else "not palindrome")

print(text.index("o"))

