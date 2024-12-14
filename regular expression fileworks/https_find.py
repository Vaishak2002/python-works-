from re import finditer

f=open("regular expression fileworks/sample_text2.txt")

for line in f:

    words=line.rstrip("\n")

    pattern="http[s]?://[a-zA-Z\W/\S]+"

    matcher=finditer(pattern,words)

    for obj in matcher:

        print(obj.group())