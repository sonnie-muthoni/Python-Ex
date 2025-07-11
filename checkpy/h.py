#compare height of three people
int1 = int(input("Enter the height of john 170 cm: "))
int2 = int(input("Enter the height of Alice 172 cm: "))
int3 = int(input("Enter the height of Bob 150 cm: "))
if int1 > int2 and int1 > int3:
    print("John is the tallest")
elif int2 > int1 and int2 > int3:
    print("Alice is the tallest")
elif int3 > int1 and int3 > int2:
    print("Bob is the tallest")
elif int1 == int2 and int1 > int3:
    print("John and Alice are the tallest")
elif int1 == int3 and int1 > int2:
    print("John and Bob are the tallest")
elif int2 == int3 and int2 > int1:
    print("Alice and Bob are the tallest")
elif int1 == int2 and int2 == int3:
    print("All three are of equal height")
else:
    print("There is an error in the input")