import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('models/linear_regression_model.pkl')

# App title
st.title("Sales Prediction App Using Linear Regression")

# Inputs
promo = st.slider("Promotion (1 = Yes, 0 = No)", min_value=0, max_value=1, step=1)
customers = st.number_input("Number of Customers", min_value=0, max_value=1000, step=1)
weekday = st.selectbox("Day of the Week", options=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Mapping weekday to numeric value (example)
weekday_mapping = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
weekday_numeric = weekday_mapping[weekday]

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'Store': [1],                  # Default store value (adjust if needed)
    'DayOfWeek': [weekday_numeric],
    'Customers': [customers],
    'Open': [1],                   # Default to "open" (adjust based on input)
    'Promo': [promo],
    'SchoolHoliday': [0],          # Default to no school holiday
    'Year': [2024],                # Default year (or dynamically get current year)
    'Month': [1],                  # Default month (or dynamically get current month)
    'Day': [1],                    # Default day (or dynamically get current day)
    'Weekday': [weekday_numeric],  # Same as DayOfWeek in this case
    'StateHoliday_a': [0],         # Default values for one-hot encoded columns
    'StateHoliday_b': [0],
    'StateHoliday_c': [0]
})

# Ensure the columns align with what the model was trained on
input_data = input_data[[
    'Store', 'DayOfWeek', 'Customers', 'Open', 'Promo', 'SchoolHoliday',
    'Year', 'Month', 'Day', 'Weekday', 'StateHoliday_a', 'StateHoliday_b', 'StateHoliday_c'
]]

# Debugging step: print to ensure all features are present
st.write("Input Data for Prediction:", input_data)

# Make predictions
if st.button("Predict Sales"):
    prediction = model.predict(input_data)
    st.write(f"Predicted Sales: {round(prediction[0], 2)}")

