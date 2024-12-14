def is_prime(num):

    is_prime1=True

    for i in range(2,num):

        if num%i==0:

            is_prime1=False
            break

    if is_prime1==True:

        print(" it is a prime")

    else:

        print("not a prime no")

is_prime(6)