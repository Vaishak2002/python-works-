start=int(input("enter the start "))

end=int(input("enter the end"))

if start>end:

    start,end=end,start
    

i=start

while(i<=end):

    if i%2!=0:

        print(i)

    i+=1