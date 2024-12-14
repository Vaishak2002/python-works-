
product={"id":1,"title":"soap","price":30,"brand":"chandrika"}

print(product["title"])

#update product price

product["price"]=50

print(product)

#update brand name

product["brand"]="cutie"

# add a field

product["use_by-date"]="10-6-2025"

print(product)

if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

print(product)