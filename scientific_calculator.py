import streamlit as st
import math

# Title of the app
st.title("Scientific Calculator")
st.write("Created by: Engineer Atique Ahmed")
# Input field for the number
num = st.number_input("Enter a number", value=0.0, format="%f")

# Select the operation
operation = st.selectbox("Choose an operation", [
    "Addition", "Subtraction", "Multiplication", "Division", 
    "Square", "Square Root", "Exponentiation", "Logarithm (base 10)", 
    "Natural Logarithm", "Sine", "Cosine", "Tangent", "Factorial"
])

# Additional input for operations requiring two numbers
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]:
    num2 = st.number_input("Enter the second number", value=0.0, format="%f")

# Perform the calculation based on the selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = num + num2
        st.write(f"The result of {num} + {num2} is {result}")
    elif operation == "Subtraction":
        result = num - num2
        st.write(f"The result of {num} - {num2} is {result}")
    elif operation == "Multiplication":
        result = num * num2
        st.write(f"The result of {num} * {num2} is {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num / num2
            st.write(f"The result of {num} / {num2} is {result}")
        else:
            st.write("Error: Division by zero is undefined.")
    elif operation == "Square":
        result = num ** 2
        st.write(f"The square of {num} is {result}")
    elif operation == "Square Root":
        if num >= 0:
            result = math.sqrt(num)
            st.write(f"The square root of {num} is {result}")
        else:
            st.write("Error: Square root of a negative number is undefined.")
    elif operation == "Exponentiation":
        result = num ** num2
        st.write(f"The result of {num} ^ {num2} is {result}")
    elif operation == "Logarithm (base 10)":
        if num > 0:
            result = math.log10(num)
            st.write(f"The logarithm (base 10) of {num} is {result}")
        else:
            st.write("Error: Logarithm of a non-positive number is undefined.")
    elif operation == "Natural Logarithm":
        if num > 0:
            result = math.log(num)
            st.write(f"The natural logarithm of {num} is {result}")
        else:
            st.write("Error: Logarithm of a non-positive number is undefined.")
    elif operation == "Sine":
        result = math.sin(math.radians(num))
        st.write(f"The sine of {num} degrees is {result}")
    elif operation == "Cosine":
        result = math.cos(math.radians(num))
        st.write(f"The cosine of {num} degrees is {result}")
    elif operation == "Tangent":
        result = math.tan(math.radians(num))
        st.write(f"The tangent of {num} degrees is {result}")
    elif operation == "Factorial":
        if num >= 0 and num == int(num):
            result = math.factorial(int(num))
            st.write(f"The factorial of {int(num)} is {result}")
        else:
            st.write("Error: Factorial is only defined for non-negative integers.")

