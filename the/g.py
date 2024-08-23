import streamlit as st

def main():
    st.title("Simple Streamlit App")

    st.write("Hello, welcome to my Streamlit app!")

    # Input from the user
    name = st.text_input("What's your name?")

    if st.button("Say Hello"):
        st.write(f"Hello, {name}!")

    # Display a simple plot
    st.write("Here's a simple line chart:")
    chart_data = [1, 2, 3, 4, 5]
    st.line_chart(chart_data)

