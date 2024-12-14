ist=[2,3,4,5]

sum=int(input("enter the no"))

left=0
right=len(ist)-1

curr_sum=0

while(left<right):

    curr_sum=ist[left]+ist[right]

    if curr_sum==sum:

        print(ist[left],ist[right])

        break

    elif curr_sum>sum:

        right-=1

    elif curr_sum<sum:

        left+=1




    


















