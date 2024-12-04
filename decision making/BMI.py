#print under weight if bmi<19
#print normal weight if bmi 19 to <25
#print overweight if bmi 25 to <30
#print obese if bmi>30

#BMI= Wght_in_kg/(height in metre)**2

weight_in_kg=int(input("enter weight in kg:"))
height_in_cm=int(input("height in cm:"))
height_in_m=height_in_cm/100
BMI=weight_in_kg/(height_in_m)**2
BMI=round(BMI)

if BMI < 19:
    print("underweight")
elif BMI <25:
    print("normal weight")
elif BMI <30 :
    print("overweight")
elif BMI >=30 :
    print("obese")