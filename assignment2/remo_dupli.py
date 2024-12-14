arr=[1,2,2,3,4,5,4,6,7]

arr.sort()

arr2=[]

for i in range(0,len(arr)-3):

    j=i+1



    result=arr[j]-arr[i]

    if result==0:

        arr.pop(j)



    
print(arr)