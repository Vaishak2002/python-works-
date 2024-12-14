
from re import finditer

f=open("/Users/vaishakj/Desktop/pythonworks/regular expression fileworks/social_post.txt","r")

for lines in f:

    word=lines.rstrip("\n")

    # word=line.rstrip(" ")

    pattern="#\w+"

    matcher=finditer(pattern,word)

    for obj in matcher:

        print(obj.group())






    