start=int(input("enter the start"))

end=int(input("entr the limit"))

for num in range(start,end):

    is_prime=True

    for i in range(2,num):

        if num%i==0:

            is_prime=False

            break

    if is_prime==True:

        print(num)