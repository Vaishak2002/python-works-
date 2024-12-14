weight_inkg=int(input("enter the weight in kg:"))
          
height= int (input("enter the height in cm"))

heigt_inmeter=height/100

bmi=weight_inkg/heigt_inmeter**2

bmi =round(bmi,2)


print(bmi)