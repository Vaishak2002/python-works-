#find the duplicate no in the array:

arr=[1,2,2,2,1,4,5]

dupli=[]

arr.sort()

for i in range(0,len(arr)-1):

    j=i+1

    result=arr[j]-arr[i]

    if result==0:

        if arr[i] not in dupli:

            dupli.append(arr[i])

print(dupli)
     



