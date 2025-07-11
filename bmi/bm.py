# Calculate body mass index (BMI)
# Get user input for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("underweight.")
elif 18.5 <= bmi <= 24.9:
    print("normal weight.")
elif 25 <= bmi <= 29.9:
    print("overweight.")
elif bmi >= 30:
    print("obesity.")
else :
    print("Invalid input.")
print("Your BMI is: ", bmi)
# Calculate the BMI
# Print the BMI category
