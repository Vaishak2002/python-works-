arr=[2,4,6,8,3,7,5]

element=int(input("enter the element to e searched"))

is_found=False

for i in range(0,len(arr)):

    if arr[i]==element:

        is_found=True

        break

print(is_found)