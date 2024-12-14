arr=[1,2,3,4,5,6,7,8,9,10]

element=int(input("enter the element to be searched"))

low=0

upp=len(arr)-1

is_found=False

arr.sort()

while(low<=upp):

    mid=(low+upp)//2





    if arr[mid]==element:

        is_found=True

        break

    elif element <arr[mid]:

        upp=mid-1

    elif element>arr[mid]:

        low=mid+1

print(is_found)
