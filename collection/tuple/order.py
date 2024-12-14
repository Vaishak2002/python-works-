order="tea coffee tea coffee gheeroast plainroast porotta tea"


orders=order.split(" ")


order_summary={}


for i in orders:


    if i in order_summary:

        order_summary[i]+=1


    else:


        order_summary[i]=1   


print(order_summary)