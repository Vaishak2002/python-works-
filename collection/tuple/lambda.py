# lambda fuction

# lambda fuction for adding 2 nums

add=lambda n1,n2:n1+n2

print(add(10,2))

# subtract 2 nums

sub=lambda n1,n2:n1-n2

print(sub(12,2))

# cube of a number

cube=lambda n:n**3

print(cube(2))

# max of 2 strings

max_2=lambda str1,str2:str1 if len(str1)>len(str2) else str2

print(max_2("hai","hello"))

# min of 2 nums

min_2=lambda str1,str2:str1 if len(str1)<len(str2) else str2

print(min_2("hai","hello"))

# smart subtract

smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(10,8))