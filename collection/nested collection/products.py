products=[
    {"id":1,"title":"s23ultra","brand":"samsung","price":78000},
    {"id":2,"title":"a17","brand":"samsung","price":18000},
    {"id":3,"title":"m50","brand":"samsung","price":16000},
    {"id":4,"title":"pocom3","brand":"poco","price":15000},
    {"id":7,"title":"vivov50","brand":"vivo","price":25000},
    {"id":5,"title":"oppof19pro","brand":"oppo","price":27000},
    {"id":6,"title":"iphone16pro","brand":"apple","price":150000},
    {"id":9,"title":"iphone16promax","brand":"apple","price":150000},
    {"id":8,"title":"nokia105","brand":"nokia","price":900}

]

# total number of mobiles

# print mobile titles

# print samsung mobiles

# # 1
# no_of_mobiles=len(products)

# print(no_of_mobiles)

# # 2

# mob_titles=[t.get("title") for t in products]

# print(mob_titles)

# # 3


# mob=[m.get("title") for m in products if m.get("brand")=="samsung"]

# print(mob)

# print the expensive mobile

# print(max(products,key= lambda d:d.get("price")))   

# prin costly mobile names

costly_mob=max(products,key=lambda d:d.get("price"))

max_price=costly_mob.get("price")

costly_mobiles=[p.get("title") for p in products if p.get("price")==max_price]

print(costly_mobiles)

# count of samsung title

samsung_mobiles=[m.get("title") for m in products if m.get("brand")=="samsung"]

count=len(samsung_mobiles)

print(count)































































































































































































































































































































































































































