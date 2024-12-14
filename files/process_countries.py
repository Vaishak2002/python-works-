from json import load

f=open("/Users/vaishakj/Desktop/pythonworks/dataset/countries.json",encoding="utf-8")

data=load(f)

# 1 print number of countries÷

# print(len(data))

# 2 print all country names==>

all_country_names=[country.get("name")  for country in data]

# print(all_country_names)

# 3 print all country "regions" ==>

all_region=[country.get("region")  for country in data]

# print(set(all_region))

# 4 print region count"" ==>

region_count={region:all_region.count(region) for region in all_region}

# print(region_count)

# 5 print max region count" ==>

max_region_count=max(region_count,key=lambda k:region_count.get(k))

# print(max_region_count)

# 6 capital of a specific country ==>"india"

capital=[ country.get("capital") for country in data if country.get("name")=="India"]

# print(capital)

# 7 print countries with most number of borders

country_border_count={country.get("name"):len(country.get("borders",[])) for country in data } 

# print(country_border_count)

# 8 print country with maximun number of borders

max_border=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

# print(max_border)

# 9 most populated country==>

max_populated=max(data,key=lambda country:country.get("population",0)).get("name")

# print(max_populated)

# 10 print the names of countries sharing borders with india 

aplfa_three_codes=[country.get("borders") for country in data if country.get("name")=="Afghanistan"][0]

for code in aplfa_three_codes:

    for country in data:

        if country.get("alpha3Code")==code:

            print(country.get("name"))