def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

try:
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive.")
    else:
        bmi, category = calculate_bmi(weight, height)
        print(f"\nBMI: {bmi:.2f}")
        print(f"Category: {category}")

except ValueError:
    print("Please enter valid numbers.")