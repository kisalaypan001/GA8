!pip install -q streamlit

import streamlit as st

def find_max(a, b, c):
    return max(a, max(b, c))

def main():
    st.title("Maximum Number Finder")

    st.write("Enter three numbers to find the maximum:")
    num1 = st.number_input("Number 1", value=0)
    num2 = st.number_input("Number 2", value=0)
    num3 = st.number_input("Number 3", value=0)

    if st.button("Find Maximum"):
        maximum = find_max(num1, num2, num3)
        st.write(f"The maximum number is: {maximum}")

if __name__ == "__main__":
    main()
