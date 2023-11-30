# login1.py
import streamlit as st
from button2 import stud

def authenticate_user(username, password):
    if username == "rathi":
        if password =="123":
            return True
    else:
        return False

def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login") == True:
        user = authenticate_user(username, password)
        if user:
            st.success("Login Successful!")
            st.session_state.logged_in = True
            stud()
        else:
            st.error("Invalid credentials. Please try again.")
