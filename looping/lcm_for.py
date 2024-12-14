num1=int(input("enter the first number"))

num2=int(input("enter the second number"))

greatest=max(num1,num2)

for i in range(greatest,(num1*num2)+1,greatest):
    
    if i%num1==0 and i%num2==0:

        print(i)

        break