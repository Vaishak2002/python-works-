text = "this is a simple question return word with maximum number of characters" 

words=text.rsplit(" ")

word_len={ word:len(word) for word in words}

print(word_len)

max_len=max(word_len,key=lambda w:word_len.get(w))

print(max_len)
