

from re import findall #to fetch the groups from thr pattern

f=open("regular expression fileworks/sample_text2.txt","r")

content=f.read()  #to read the entire content

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)