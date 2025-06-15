#check voter eligibility
age = int(input("Enter your age: "))
citizen= input("Enter your country of citizenship UGANDA,TANZANIA,KENYA : ").strip().upper()
if age >= 18 and citizen in ["UGANDA", "TANZANIA", "KENYA"]:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
