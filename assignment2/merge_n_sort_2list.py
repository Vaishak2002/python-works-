arr1=[1,4,3,2,5]

arr2=[8,7,6,10,9]


for i in range(0,len(arr2)):

    arr1.append(arr2[i])

arr1.sort()

print(arr1)