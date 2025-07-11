salary = int(input("Enter your salary: ")) 
year = int(input("Enter the years worked: "))   

if (year < 10):
    bonus = salary * 0.1
elif (year >= 6 and year <= 10):
    bonus = salary * 0.2
elif (year < 6):
    bonus = salary * 0.3
else:
    print("Invalid input")
    bonus = 0

print("Your bonus is: ", bonus)

total = salary + bonus
print("Your total salary is: ", total)