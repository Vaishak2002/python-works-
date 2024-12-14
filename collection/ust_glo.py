#input=[100,200,300,400,500,600,700,800]

#output=[100,800,300,600,500,400,700,200]

arr=[100,200,300,400,500,600,700,800]

arr_odd=[]

for i in range(1,len(arr),2):
 
    arr_odd.append(arr[i])


arr_odd.reverse()

print(arr_odd)

j=0

for i in range (1,len(arr),2):

    arr.pop(i)

    arr.insert(i,arr_odd[j])

    j+=1

print(arr)

