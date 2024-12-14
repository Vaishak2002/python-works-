arr1=[2,3,5,4,6]

arr2=[3,8,9,4,1,11,6]

common=[]

for i in range(0,len(arr1)):

    for j in range(0,len(arr2)):

        if arr1[i]==arr2[j]:

            common.append(arr1[i])

            break

print("common elements in both lists are",common)


