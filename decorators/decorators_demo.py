
def swap_decorator(fn):    #decorator always recieves an other function, where "fn" are the functions called below

    def wrapper(n1,n2):

        if n1<n2:
                                  #body of the function "wrapper"
            (n1,n2)=(n2,n1)

        return fn(n1,n2)
    
    return wrapper     #result of wrapper is returned to the functions by calling it

def round_decorator(fn):

    def wrapper(num1,num2):

        num1=round(num1)
        num2=round(num2)

        return fn(num1,num2)
    
    return wrapper


@round_decorator
@swap_decorator
def add_numbers(num1,num2):

    return num1+num2

@round_decorator
@swap_decorator
def smart_sub(num1,num2):

    return num1-num2

@round_decorator
@swap_decorator
def smart_div(num1,num2):

    return num1/num2

# print(smart_sub(10,2))

# print(smart_sub(2,10))

# print(smart_div(10,2))

# print(smart_div(2,10))

# print(add_numbers(10,2))

# print(add_numbers(2,10))

print(add_numbers(2.8,3.4))