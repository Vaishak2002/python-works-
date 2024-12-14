def perfect(num):
    no=0
    for i in range(1,num):

        if num%i==0:

            no+=i

    print ("perfect no" if num==no else "not perfect")


perfect(16)