text="this is a test to remove duplicate words this test is simple"

# split the text with space 

words=text.split(" ")

text2="this simple test remove duplicate words"

word2=text2.split(" ")

print(set(words).issubset(set(word2)))



