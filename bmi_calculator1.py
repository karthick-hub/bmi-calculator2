def calculate_bmi(weight, height):
    """Calculate BMI given weight in kilograms and height in meters."""
    bmi = weight / (height ** 2)
    return bmi

def get_positive_float(prompt):
    """Prompt the user until they enter a valid positive float."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be a positive number. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("BMI Calculator")

    weight = get_positive_float("Enter your weight in kilograms: ")
    height = get_positive_float("Enter your height in meters: ")

    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi < 25:
        print("Category: Normal weight")
    elif 25 <= bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")

if __name__ == "__main__":
    main()