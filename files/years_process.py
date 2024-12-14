
years_path="dataset/year.txt"

century_years="dataset/century_years.txt"

leap_year="dataset/leap_years.txt"


f_year=open(years_path,"r")

f_century=open(century_years,"w")

f_leapyear=open(leap_year,"w")

def is_leapyear(year):

     return True if year%100==0 and year%400==0 or year%100!=0 and year%4==0 else False

def is_century_year(year):
     
     return True if year%100==0 else False

for year in f_year:
     
     year=int(year)
     
     if is_century_year(year)==True:
          
          f_century.write(str(year)+"\n")

     if is_leapyear(year)==True:

          f_leapyear.write(str(year)+"\n") 


f_year.close()

f_century.close()

f_leapyear.close()

