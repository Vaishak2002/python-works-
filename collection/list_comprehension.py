#list comprehension

#Syntax:

#reference=[return loop condition]

#eg:

arr=[2,3,4,5,6,7,8]

add_three=[num+3 for num in arr]

print(add_three)

#eg 2: square of elements in the array

square=[num**2 for num in arr]

print(square)

#even numbers:

even_num=[num for num in arr if num%2==0]

print(even_num)

#num greater than 5:

num_gt_5=[num for num in arr if num>5]

print(num_gt_5)

# list with num+1 if num greater than 5  else num-1

new_list=[num+1 if num>5 else num-1 for num in arr]

print("\n",new_list)

# wiords starting with vowels:

text=["apple","iphone","orange","potatto"]

vowels=[num for num in text if num[0]  in ['a','e','i','o','u'] ]


print(vowels)

# comsonents

text2=["apple","iphone","orange","potatto"]

consonents=[w for w in text2 if w[0] not in ['a','e','i','o','u']]

print(consonents)

# longest word

text3=["apple","iphone","orange","potatto","tomatto"]

long=max([len(w) for w in text3 ])

longest_word=[w for w in text3 if len(w)==long]

print(longest_word)

