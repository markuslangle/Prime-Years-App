import streamlit as st

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

st.title("Prime Years")

birth_year = st.number_input("What year were you born?", min_value=1900, max_value=2100, step=1)
lifespan = st.number_input("How many years do you plan to live?", min_value=1, max_value=150, step=1)

if birth_year and lifespan:
    st.subheader("Your Prime Years:")
    prime_years = []
    for age in range(1, lifespan + 1):
        if is_prime(age):
            year = birth_year + age
            prime_years.append((year, age))
    for year, age in prime_years:
        st.write(f"Year: {year}, Age: {age} (Prime)")
