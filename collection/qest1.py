arr=[100,200,300,400,500]

k=int(input("enter the iteration"))

for i in range(1,k+1):
    
    pop_el=arr.pop()

    arr.insert(0,pop_el)

print(arr)