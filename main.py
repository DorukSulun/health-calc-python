print("\t---Welcome to Personal Health Calculator---") 

weight = float(input("\n\t\tEnter your weight(kg): "))
height_cm = float(input("\n\t\tEnter your height(cm): "))
age = int(input("\n\t\tEnter your age: "))
gender = input("\n\t\tEnter your gender(m/f): ").lower()

#height cm -> meter
height_m = height_cm/(10**2)

#calculate BMI
bmi = weight/(height_m**2)

if gender == 'm':
    bmr = 88.362 + (13.397 * weight) + (4.799 * height_cm) - (5.677 * age)
else:
    bmr = 447.593 + (9.247 * weight) + (3.098 * height_cm) - (4.330 * age)