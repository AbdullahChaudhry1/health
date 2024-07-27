def weight_status(age: int, weight: float, gender: str) -> tuple[str, str, int]:
    if age < 18:
        if weight < 40:
            status = "Slim"
            diet_plan = ("You are underweight. It's important to eat a balanced diet with enough calories. "
                         "Include protein-rich foods, whole grains, fruits, and vegetables. Avoid skipping meals "
                         "and consider adding healthy snacks.")
            calories = 3000  # Recommended daily intake to gain weight for teens
        elif 40 <= weight <= 60:
            status = "Healthy"
            diet_plan = ("You have a healthy weight. Continue maintaining a balanced diet with a variety of nutrients. "
                         "Ensure you stay active and drink plenty of water.")
            calories = 2500  # General daily caloric intake
        else:
            status = "Overweight"
            diet_plan = (
                "You are overweight. Focus on a diet rich in fruits, vegetables, lean proteins, and whole grains. "
                "Avoid sugary drinks and high-calorie foods. Regular physical activity is also essential.")
            calories = 2000  # Recommended daily intake to lose weight for teens
    else:
        if weight < 50:
            status = "Slim"
            diet_plan = ("You are underweight. It's important to eat a balanced diet with enough calories. "
                         "Include protein-rich foods, whole grains, fruits, and vegetables. Avoid skipping meals "
                         "and consider adding healthy snacks.")
            calories = 2500  # Recommended daily intake to gain weight for adults
        elif 50 <= weight <= 80:
            status = "Healthy"
            diet_plan = ("You have a healthy weight. Continue maintaining a balanced diet with a variety of nutrients. "
                         "Ensure you stay active and drink plenty of water.")
            calories = 2000  # General daily caloric intake for adults
        else:
            status = "Overweight"
            diet_plan = (
                "You are overweight. Focus on a diet rich in fruits, vegetables, lean proteins, and whole grains. "
                "Avoid sugary drinks and high-calorie foods. Regular physical activity is also essential.")
            calories = 1500  # Recommended daily intake to lose weight for adults

    return status, diet_plan, calories


# Get user's age, weight, and gender
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
gender = input("Enter your gender (male/female): ").strip().lower()

# Determine weight status, diet plan, and calorie recommendation
status, diet_plan, calories = weight_status(age, weight, gender)

# Display the result
print(f"Weight Status: {status}")
print(f"Diet Plan: {diet_plan}")
print(f"Recommended Daily Calories: {calories}")
