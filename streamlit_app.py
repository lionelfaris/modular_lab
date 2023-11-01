import streamlit as st
import math_operations as math

st.title("Simple Calculator")

x = st.number_input("Enter the first number:")
y = st.number_input("Enter the second number:")

operation = st.selectbox("Select an operation", 
                        ("Add", "Subtract", "Multiply", "Divide", "Root of numbers", "Powers of numbers"))

result = None

if st.button("Calculate"):
    if operation == "Add":
        result = math.add(x, y)
    elif operation == "Powers of numbers" :
        result = math.powers_of_numbers(x,y)
    elif operation == "Root of numbers" :
        result = math.root(x,y)
    elif operation == "Subtract":
        result = math.subtract(x, y)
    elif operation == "Multiply":
        result = math.multiply(x, y)
    elif operation == "Divide":
        try:
            result = math.divide(x, y)
        except ZeroDivisionError:
            st.error("Division by zero is not allowed.")

if result is not None:
    st.success(f"Result: {result}")
