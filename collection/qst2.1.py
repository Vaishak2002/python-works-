arr1=[4,2,6,3,7,8,9]

arr2=[6,1,5,4,8,10,9]

arr1.sort()

arr2.sort()

p1=0

p2=0

while(p1<len(arr1) and p2<len(arr2)):

    if arr1[p1]==arr2[p2]:

        print(arr1[p1])

        p1+=1
        p2+=1

    elif arr1[p1]<arr2[p2]:

        p1+=1

    elif arr1[p1]>arr2[p2]:
        
        p2+=1
