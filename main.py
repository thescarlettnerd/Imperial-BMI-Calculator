height = input("Please enter your height in inches:\n")
weight = input("Please enter your weight in pounds:\n")
h = float(height)
w = float(weight)
bmi = (w / h ** 2 * 703)
print("Your BMI is:")
print(int(bmi))