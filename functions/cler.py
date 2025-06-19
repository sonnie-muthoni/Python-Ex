#function that adds two numbers together
def addition(x,y,z):
    sum = x + y+ z
    return sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
output = addition(num1, num2, num3)
print("The sum of the three numbers is:", output)
