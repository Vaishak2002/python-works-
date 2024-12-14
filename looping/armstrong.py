num=int(input("enter the number"))

original=num

total=0

count=len(str(num))

print(f"count is {count}")

while(num!=0):

    digit=num%10

    digit=digit**count

    total=total+digit

    num=num//10

print(total)

if total==original:

    print("is armstrong")

else:

    print("is not armstrong")