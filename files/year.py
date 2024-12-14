#print years 1800 to 2024

f=open("dataset/year.txt","w")

for years in range(1800,2025):

    f.write(str(years)+"\n")


f.close()