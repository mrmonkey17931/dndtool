import random
import streamlit as st

st.title("DnD Tool")

if st.button("Roll a 20-Sided Die"):
    roll = random.randint(1,20)
    st.success(f"You rolled {roll}!")