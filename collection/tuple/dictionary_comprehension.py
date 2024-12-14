
arr=[10,20,30,40,2,3]

result={num:num**3 for num in arr }

print(result)

#even squares

even_sqr={num:num**2 for num in arr if num%2==0}

print(even_sqr)

odd_sqr={num:num**3 for num in arr if num%2!=0}

print(odd_sqr)

