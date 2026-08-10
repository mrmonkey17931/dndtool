
import random
import streamlit as st
#testing out tabs on streamlit
#when you want to add more add a new title into the st.tabs and continue
def show_dice_roller():
    dice_tab = st.tabs(["Dice Roller"])[0]

    dice_sides = dice_tab.selectbox("Choose your die", [4, 6, 8, 10, 12, 20, 100])

    dice_tab.header("Roll the Dice")
    if dice_tab.button("Roll Die"):
        roll = random.randint(1,dice_sides)
        dice_tab.success(f"You rolled a d{dice_sides} and got: {roll}!")