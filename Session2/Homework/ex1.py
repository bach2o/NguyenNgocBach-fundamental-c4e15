x = int(input("Enter your height in centimeters"))/100
y = int(input("Enter your weight in kilograms"))
BMI= y / (x*x)
print("Your BMI(Body Mass Index) is", BMI)
if BMI < 16:
    print("You are severely underweight.")
elif 16 <= BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI < 25:
    print("You are normal.")
elif 25 <= BMI < 30:
    print("You are overweight.")
else:
    print("You are obese.")
