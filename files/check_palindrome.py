
word_path="dataset/word2.txt"

write_path="dataset/palindrome.txt"

f_read=open(word_path,"r")

f_write=open(write_path,"w")

for line in f_read:

    word=line.rstrip('\n')

    reversed_word=word[::-1]

    if word==reversed_word:

        f_write.write(word+"\n")

f_read.close()

f_write.close()








