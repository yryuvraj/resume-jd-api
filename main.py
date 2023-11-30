# main.py
import streamlit as st
from login1 import login
from signup1 import signup
from button2 import stud
from recruiter import recruiter_home
from student import final

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        role = st.experimental_get_query_params().get("role", [""])[0]
        if role == 'recruiter':
            recruiter_home("aryan")
        elif role == 'student':
            final()
        else:
            stud()
    else:
        login()
        signup()

if __name__ == "__main__":
    main()
