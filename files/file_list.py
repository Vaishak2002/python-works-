f=open("dataset/words1.txt","r")

word=[]

for line in f:

    line=line.rstrip("\n")

    all_words=line.split(" ")

    for w in all_words:

        word.append(w)

       



print(word)

word_count={w:word.count(w)  for w in word}

nested_word_count=[ [v,k] for k,v in word_count.items()]  #important

print("\n",sorted(nested_word_count,reverse=True))


