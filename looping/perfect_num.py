num=int(input("enter the number"))

tot=0


for i in range(1,num):

    if num%i==0:

        tot+=i

print(" perfect number" if tot==num else "not perfect")

