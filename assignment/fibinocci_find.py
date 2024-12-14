prev=0

curr=1

num=int(input("enter the no to be found")) 

print(prev)

print(curr)



for i in range(1,10):

    next=prev+curr

    prev=curr

    curr=next

    print(next)

    if next==num:

        not_f=False

        break
    
    else:

        not_f=True

        

if not_f==True:

    print("not found")

else:

    print("no is found")
