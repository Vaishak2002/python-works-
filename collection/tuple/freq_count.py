arr=[10,20,30,40,10,20,10,30]

# freq_count={num:arr.count(num) for num in arr}

# print(freq_count)

text="ABABBCCDDE"

# char_freq={ch:text.count(ch) for ch in text }

# print(char_freq)

#non recursive elemenets

# no_recurs={ch:text.count(ch) for ch in text if text.count(ch)<2 }

# print(no_recurs)

words=["hello","hai","hello","this","is","this","is","hello"]

word_freq={ w:words.count(w) for w in words  }

print(word_freq)

recursive_word=[k for k,v in word_freq.items() if v>1]

print(recursive_word)

#display non recursive words

non_recur=[k for k,v in word_freq.items() if v<2]

print(non_recur)

#most recursive


