weight_inkg=int(input("enter the weight in kg:"))
          
height= int (input("enter the height in cm"))

heigt_inmeter=height/100

bmi=weight_inkg/heigt_inmeter**2

bmi=round(bmi,2)

if bmi<19:

    print("under weight")

elif bmi>=19 and bmi<25:

    print("normal")

elif bmi>=25 and bmi<30:

    print("over weight")