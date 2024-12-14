student_data={
    "hari":[45,40,35],
    "vipin":[34,40,45],
    "bijoy":[33,38,35],
    "anvin":[32,30,40]
    }

# if index =1 print avg mark of hari

# for index,element in enumerate(student_data):

#     print(index,element)

# index=int(input("enter the index"))

# for i,element in enumerate(student_data):

#     if i+1==index:

#         print(element)

#         marks=student_data.get(element)

#         avg=sum(marks)/len(marks)

#         print(avg)

# with key as "hari"

name=input("enter the name")

for i,element in enumerate(student_data):

    if element==name:

        print(element)

        marks=student_data.get(element)

        avg=sum(marks)/len(marks)

        print(avg)

        