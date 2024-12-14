f=open("dataset/all_students.txt","r")

all_stud=set()

failed_stud=set()

pass_studs=[]

for line in f:

    line=line.rstrip("\n")

    all_stud.add(line)

f1=open("dataset/failed_stud.txt","r")

for line in f1:

    line=line.rstrip("\n")

    failed_stud.add(line)

pass_studs=all_stud.difference(failed_stud)

print("\n",pass_studs)

