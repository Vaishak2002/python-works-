arr=[1,2,3,2,4,5,3,1]

occ_1=0
occ_2=0
occ_3=0
occ_4=0
occ_5=0

for i in range(0,len(arr)):

    if arr[i]==1:

        occ_1+=1

    elif arr[i]==2:

        occ_2+=1

    elif arr[i]==3:

        occ_3+=1

    elif arr[i]==4:

        occ_4+=1

    elif arr[i]==5:

        occ_5+=1

print(f"occurance of: 1 is:" ,occ_1,"\n\t 2 is:",occ_2,"\n\t3 is:",occ_3,"\n\t4 is:",occ_4,"\n\t5 is:",occ_5 )