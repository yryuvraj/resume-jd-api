import streamlit as st
import os
import sqlite3
from hashlib import sha256
import random
from googletrans import Translator
import chatbotCore
import pdfbot
from category import compare_resume_jd

# Define the path to the logo image
logo_path = "logo.png"

# List of interesting facts
facts = ["The average modern electronic device has more than 35 minerals in it.",
         "The first metals to be unearthed were gold and copper.",
         "The oldest known mine is believed to be the Lion Cave in Swaziland",
         # Add more facts as needed
         ]

# Function to display the logo in the sidebar
def display_logo():
    st.sidebar.image(logo_path)

# Function to navigate to the ChatBot page
def navigate_to_chatbot():
    st.session_state.menu = "ChatBot"

# Function to navigate to the PDF Reader page
def navigate_to_pdf_reader():
    st.session_state.menu = "PDF_Reader"

# Function to navigate to the Mobile Device feature page
def navigate_to_mobile_device():
    st.session_state.menu = "Mobile_Device"

# Function to display the home page content
def home_page():
    display_logo()
    st.title("🤖 MineDroid")
    st.header("Welcome to the Home Page!")
    st.write("### Select your Option from the Sidebar selectbox! 😃 \n--------")
    st.write("### Our Mission:")
    st.write("##### Our mission is to empower individuals, including those without specialized legal knowledge, with easy access to comprehensive information on Indian mining laws, rules, and regulations...")
    # Add more content as needed

# Function to display the ChatBot page content
def chatbot_page():
    display_logo()
    st.title("🧠 ChatBot Page")
    st.write("This is the Chat_Bot Page. Here, you can ask your queries in any language.")
    user_input = st.text_input("Enter your query:")

    if st.button("Ask"):
        if user_input:
            st.write("#### Fun fact while the bot is thinking: " + facts[random.randint(0, len(facts) - 1)])
            response = chatbotCore.run_chatbot(user_input)
            st.write("## Bot's Response:")
            st.write("#### " + response)
        else:
            st.warning("Please enter a query before clicking 'Ask'.")

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
    compare_resume_jd()
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
def final():
    # if "logged_in" not in st.session_state:
    #     st.session_state.logged_in = False

    # if st.session_state.logged_in:
    #     stud()
    menu = st.sidebar.selectbox("Navigation", ["Home", "ChatBot", "PDF_Reader", "Mobile_Device", "Contact"])
    # else:
    #     login()
    #     signup()
    #     st.stop()

    if menu == "Home":
        home_page()
    elif menu == "ChatBot":
        chatbot_page()
    elif menu == "PDF_Reader":
        pdf_reader_page()
    elif menu == "Mobile_Device":
        mobile_device()
    elif menu == "Contact":
        contact_page()

if __name__ == "__main__":
    final()
