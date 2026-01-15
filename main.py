print("\t---Welcome to Personal Health Calculator---") 

isContinue = True
while isContinue:
    isContinue = False
    weight = float(input("\n\t\tEnter your weight(kg): "))
    height_cm = float(input("\n\t\tEnter your height(cm): "))
    age = int(input("\n\t\tEnter your age: "))
    gender = input("\n\t\tEnter your gender(m/f): ").lower()

    #height cm -> meter
    height_m = height_cm/(10**2)

    #height cm -> inch
    height_inch = height_cm * 0.3937

    #calculate BMI
    bmi = weight/(height_m**2)

    #calculate water requirement
    water_requirenment = weight * 0.035

    if gender == 'm':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height_cm) - (5.677 * age)
        ibw = 50 + 2.3 * (height_inch-60)                                           #calculate to IBW(Ideal body weight)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height_cm) - (4.330 * age)
        ibw = 45.5 + 2.3 * (height_inch - 60)

    print("\n" + "-" * 60)
    print("\n")
    print(f"\t\tYour BMI: {round(bmi,2)}")
    print(f"\n\n\t\tYour BMR: {round(bmr,2)}")
    print(f"\n\n\t\tYour daily water requirenment: {round(water_requirenment,2)}")
    print("\n\n\t\t[NOTE]: IBW calculation is most accurate for adults over 152 cm (5 feet).")
    print(f"\t\tYour IBW(ideal body weight): {round(ibw,2)}")
    print("\n" + "-" * 60)
    ans = input("Do you want to continue(y/n): ").lower()
    if ans == 'y':
        isContinue = True