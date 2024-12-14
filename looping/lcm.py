num1=int(input("enter the first number"))

num2=int(input("enter the second number"))

lcm=0

if num1>num2:
    
    greater=num1

else:

    greater=num2

if greater%num1==0 and greater%num2==0:

    print(f"{greater} is lcm of {num1}and{num2}")

else:
     
     lcm=num1*num2

     print(f"lcm of {num1} and {num2} is {lcm}")