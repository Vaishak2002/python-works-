weight=int(input("enter weight in kg"))

height=int(input("enter height in cm"))

age=int(input("enter the age"))

gender=input("enter your gender").lower()

if gender=="male":

    bmr=10*weight+6.25*height-5*age+5

    print(f"bmr value is {bmr}")

elif gender=="female":

    bmr=10*weight+6.25*height-5*age-161

    print(f"bmr value is {bmr}")

else:

    print("error")

activity_level= int(input("""select activity level
        press 1 for sedentary
              2 for light activity
              3 for moderate activity
              4 for very active
              5 for extra active """
)) 

if activity_level==1:

    calories=bmr*1.2

elif activity_level==2:

    calories=bmr*1.375

elif activity_level==3:

    calories=bmr*1.55

elif activity_level==4:

    calories=bmr*1.725

elif activity_level==5:

    calories=bmr*1.9

else:

    print("invalid activity")

print("total calories to maintained = ",calories)

target_weight= int(input("enter the weight to reduce in kg"))

duration= int(input("enter the duration in weeks"))

calorie_defecit=target_weight*7700

days=duration*7

daily_cal_deficit=calorie_defecit/days

print(f" daily calorie intake to be followed to reduce {target_weight} kg in {duration} weeks is {daily_cal_deficit} calories")








