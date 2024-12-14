arr=[1,2,3,4,5,6]

index=int(input("enter the index"))

try:

    num=arr[index]

    print(num)

except Exception as e:

    print('error occured')

    print(e)

