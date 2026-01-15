print("\t---Welcome to Personal Health Calculator---") 

weight = float(input("\n\tEnter your weight(kg): "))
height_cm = float(input("\n\tEnter your height(cm): "))
age = int(input("\n\tEnter your age: "))
gender = input("\n\tEnter your gender(m/f): ").lower()

#height cm -> meter
height_m = height_cm/(10**2)

#calculate BMI
bmi = weight/(height_m**2)
