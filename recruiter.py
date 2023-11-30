import streamlit as st
import firebase_admin
from firebase_admin import credentials, storage

# cred = credentials.Certificate('/Users/devkumar/Desktop/rohan_major/MineDroid/web-app-cf27c-firebase-adminsdk-2ql98-e312321687.json')
#firebase_admin.initialize_app(cred, {'storageBucket': 'web-app-cf27c.appspot.com'})

def upload_to_firebase(file_content, filename):
    # Upload the file to Firebase Storage
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_string(file_content, content_type='application/pdf')

def recruiter_home(username):
    st.title("Recruiter Home")
    st.sidebar.title(f"Welcome, {username}")

    # Display initial text and paragraph
    st.write(f"Welcome, Recruiter {username}!")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eget velit nec sapien vestibulum rhoncus. Maecenas vitae risus id tellus hendrerit mattis.")
    st.write("More features and information for recruiters can be added here.")

    # Options in the sidebar
    option = st.sidebar.selectbox("Select an option", ["Recruiter Home", "Post a job"])

    # Track whether the user selected "Post a job"
    post_job_selected = option == "Post a job"

    if post_job_selected:
        # Form input for job details
        st.write("## Job Details:")
        company_name = st.text_input("Company Name:")
        hr_name = st.text_input("HR Name:")
        hr_email = st.text_input("HR Email:")
        ctc = st.text_input("CTC:")
        job_profile = st.text_input("Job Profile")

        # File upload
        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

        if uploaded_file is not None:
            # Display the PDF
            st.write("Uploaded PDF:")
            st.write(uploaded_file)

            # Convert the PDF file to bytes
            file_content = uploaded_file.read()

            # Get the filename
            filename = uploaded_file.name

            # Upload the PDF to Firebase
            upload_to_firebase(file_content, filename)

            st.success("PDF file successfully uploaded to Firebase Storage!")

            # Display job details
            st.write("## Job Details Summary:")
            st.write(f"**Company Name:** {company_name}")
            st.write(f"**HR Name:** {hr_name}")
            st.write(f"**HR Email:** {hr_email}")
            st.write(f"**CTC:** {ctc}")
            st.write(f"**Job Profile:** {job_profile}")

if __name__ == "__main__":
    recruiter_home("YourRecruiterUsername")
