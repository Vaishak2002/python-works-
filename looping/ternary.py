# true expression if conditionelse false expression

num=10

result="+ve" if num>0  else "-ve"

print(result)

#print even no with ternary function

start=int(input("enter start"))

end=int(input("enter the end"))

reverse=True if start>end else False

i= start

while(i<=end if reverse==False else i>=end):

    if(i%2==0):

        print(i)

    if reverse==False:

        i+=1

    else:

        i-=1
        


