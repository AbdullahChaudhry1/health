import streamlit as st


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


# Streamlit app
st.title("Abdullah Weight Status and Diet Plan")

# User input
age = st.number_input("Enter your age:", min_value=1, max_value=150, value=25)
weight = st.number_input("Enter your weight (kg):", min_value=0.0, value=70.0, step=0.1)
gender = st.selectbox("Select your gender:", options=["male", "female"])

# Calculate weight status and recommendations
status, diet_plan, calories = weight_status(age, weight, gender)

# Display results
st.write(f"**Weight Status:** {status}")
st.write(f"**Diet Plan:** {diet_plan}")
st.write(f"**Recommended Daily Calories:** {calories}")
