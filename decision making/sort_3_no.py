num1=int(input("enter 1st no"))

num2=int(input("enter 2nd no"))

num3=int(input("enter 3rd no"))

if num1==num2 and num1==num3:

    print("the numbers are equal")


elif num1>num2 and num1>num3:

    if num2>num3:

        print("sorted order",num1,num2,num3)
    
    else:

        print("sorted order is",num1,num3,num2)

elif num2>num1 and num2>num3:

    if num1>num3:

        print("sorted order is",num2,num1,num3)
    
    else:

        print("sorted order is",num2,num3,num1)

elif num3>num1 and num3>num2:

    if num2>num1:

        print("sorted order is" ,num3,num2,num1)
    
    else:

        print("sorted order is" ,num3,num1,num2)




