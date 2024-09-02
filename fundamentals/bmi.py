#program to calculate bmi-body mass index

#bmi=(weight in kg/height in meter squared)

weight_in_kg=int(input("Enter weight: "))

height_in_cm=int(input("Enter height: "))

height_in_m=height_in_cm/100

bmi=weight_in_kg/height_in_m**2

print(f"BMI={bmi}")

if bmi <= 19:

    print("\nUnder Weight")

elif bmi<=25:

    print("\nNormal Weight")

elif bmi<=30:

    print("\nOver Weight")

else:

    print("Obesity")