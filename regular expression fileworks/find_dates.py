
from re import finditer

f=open("/Users/vaishakj/Desktop/pythonworks/regular expression fileworks/dates_text.txt","r")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

dates=finditer(pattern,content)

for date in dates:

    print(date.group())