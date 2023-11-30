import streamlit as st
import os
import sqlite3
from hashlib import sha256
import random
from googletrans import Translator
import chatbotCore
import pdfbot
from button2 import stud
# Define the path to the logo image
logo_path = "logo.png"

# Function to display the logo in the sidebar
def display_logo():
    st.sidebar.image(logo_path)

# Function to display the PDF Reader page content
def pdf_reader_page():
    display_logo()
    st.title("📖 PDF Reader!")
    st.write("This is the PDF reader!")
    st.write("Here, you can upload any PDF of yours and ask questions regarding it!")
    pdfbot.pdf_reader()

# Function to display the Mobile Device feature page content
def mobile_device():
    display_logo()
    st.title("Mobile Device Feature")
    st.write("This is the Mobile Device Feature page.")
    st.write("You can use the application on your mobile remote device here.")
    # Add more content as needed

# Function to display the Contact page content
def contact_page():
    display_logo()
    st.title("Contact Page")
    st.write("Contact us at contact@example.com")
    # Add more content as needed

# Function to create a database connection
def create_connection():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create the user table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    return conn

# Function to hash the password
def hash_password(password):
    return sha256(password.encode()).hexdigest()

# Function to add a new user to the database
def add_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)

    cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', (username, hashed_password))

    conn.commit()
    conn.close()

# Function to authenticate a user
def authenticate_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)

    cursor.execute('''
        SELECT * FROM users
        WHERE username = ? AND password = ?
    ''', (username, hashed_password))

    user = cursor.fetchone()
    conn.close()

    return user

# Function to handle user login
def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = authenticate_user(username, password)
        if user:
            st.success("Login Successful!")
            st.session_state.logged_in = True
        else:
            st.error("Invalid credentials. Please try again.")

# Function to handle user signup
def signup():
    st.title("Signup Page")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if new_password == confirm_password:
            add_user(new_username, new_password)
            st.success("Signup Successful! You can now log in.")
        else:
            st.error("Passwords do not match. Please try again.")

# Main function to handle page navigation based on user authentication
def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        stud()
        # menu = st.sidebar.selectbox("Navigation", ["Home", "ChatBot", "PDF_Reader", "Mobile_Device", "Contact"])
    else:
        login()
        signup()
        st.stop()

    # if menu == "Home":
    #     home_page()
    # elif menu == "ChatBot":
    #     chatbot_page()
    # elif menu == "PDF_Reader":
    #     pdf_reader_page()
    # elif menu == "Mobile_Device":
    #     mobile_device()
    # elif menu == "Contact":
    #     contact_page()

if __name__ == "__main__":
    main()



















