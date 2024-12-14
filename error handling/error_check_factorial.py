def is_factorial(num):

    factorial=1

    while num!=0:
        
        factorial=factorial*num%10

        num-=1

    print(factorial)

is_factorial(3)