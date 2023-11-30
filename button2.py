# button2.py
import streamlit as st
import urllib.parse

def stud():
    st.title("Recruiter or Student?")
    st.write("Please select your role:")
    
    # Set the width and height for the buttons
    button_width = 100
    button_height = 100

    # Add custom CSS to control button width, height, and margin
    st.markdown(
        f"""
        <style>
            div.stButton > button {{
                width: {button_width}px;
                height: {button_height}px;
                position: relative;
                margin-left: 10%;  /* Adjust the margin as needed */
            }}
            
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    col1, col2 = st.columns(2)
    
    # Button to indicate if the user is a recruiter
    with col1:
        recruiter_button = st.button("Are you a recruiter?")
        if recruiter_button:
            # Set the URL parameter to 'role=recruiter'
            st.experimental_set_query_params(role='recruiter')
            
    with col2:
        # Use st.image within the button to display an image
        if st.button("Are you a Student ? 🎓"):
            # Set the URL parameter to 'role=student'
            st.experimental_set_query_params(role='student')
