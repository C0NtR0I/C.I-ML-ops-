import streamlit as st 

st.title("Power Calculator")
st.write("Enter the number to calculate is Square,Cube and Fifth power")

n=st.number_input("Enter Integer",value=1, step=1)

square = n ** 2
cube = n ** 3
fifth_power = n ** 5

# Display results
st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")

