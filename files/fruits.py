f=open("dataset/fruits.txt","r")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))   # "rstrip " is used to strip chars from the list while printing 

print(fruits)