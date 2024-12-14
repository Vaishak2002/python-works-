# append  method

color=["red","green","blue"]

color.append("yellow")

print(color)

#color.pop()  : which removes the last object from the 'list'abs

color.pop()

print(color)

color.pop(1)  # removes the object in the index position '1' from the list

print(color)

# to insert an object:

color.insert(0,"purple")   # used to insert an 'object' at any given 'index' in a 'list'

print(color)

# "index" finding method

red_index=color.index("red")

print(red_index)


# "copy" method : 

abhi_fav_color=["red","blue","black","white"]

xav_fav_color=abhi_fav_color.copy()

xav_fav_color.pop()

print(abhi_fav_color)

print(xav_fav_color)

# sort method:

lst=[4,3,2,6,1,7]

# lst.sort()  : sorted in ascending order

lst.sort(reverse=True)  # sortrd in descending order

print(lst)

#extends method

fruits=["apple","orange","mango"]

products=["onion","potat","brinjal"]

products.extend(fruits)

print(products)
