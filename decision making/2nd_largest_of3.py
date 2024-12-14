num1=int(input("enter 1st no"))

num2=int(input("enter 2nd no"))

num3=int(input("enter 3rd no"))

if num1==num2 and num1==num3:

    print("the numbers are equal")


elif num1>num2 and num1>num3:

    if num2>num3:

        print("num2 is second largest")
    
    else:

        print("num3 is second largest")
elif num2>num1 and num2>num3:

    if num1>num3:

        print("num1 is second largest")
    
    else:

        print("num3 is second largest")

elif num3>num1 and num3>num2:

    if num2>num1:

        print("num2 is second largest")
    
    else:

        print("num1 is second largest")




