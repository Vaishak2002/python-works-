text="this is a simple programing question to find word with maximum number of characters"

# words=text.split(" ")

# def get_length(w):

#     return len(w)

# print(max(words,key=get_length))


# words=text.split(" ")

# def get_length(w):

#     return len(w)

# srt_words=sorted(words,key=get_length,reverse=True)

# print(srt_words)

# most recursive word==>

words=text.split(" ")

def get_count(w):

    return words.count(w)

frequent_word=max(words,key=get_count)

print(frequent_word)

