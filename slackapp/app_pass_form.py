import os
import streamlit as st
from supabase import create_client
from dotenv import load_dotenv
load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase_client = create_client(supabase_url, supabase_key)

def store_app_password(email, app_passwords, supabase_client):
    """Stores the passwords in the Supabase database."""
    try:
        supabase_client.table('slack_app').update({'app_passwords': app_passwords}).match({'email': email}).execute()
        st.write("Success, You can now close and go back to the app")
    except Exception as e:
        st.write(f"An error occurred. Try again")

def main():
    st.title('Instructions to Enable Email Sending Feature')

    st.markdown("""
    ## Creating a Google App password
               
    1. Visit the 2-Step Verification page on your Google Account using this [link](https://myaccount.google.com/signinoptions/two-step-verification/enroll-welcome). You might need to sign in.
    2. If you don’t have 2-Step Verification on your Google Account, you’ll need to set it up.
    3. Once 2-Step Verification is enabled, go back to the 2-Step Verification page in the Security Tab under "How to Sign-in to Google" and scroll down to select **App passwords**. 
    4. Select the App Passwords, and create a new app specific name, we suggest 'MailQA' click on create.
    5. Copy the 16 character code into the field below.
    6. This does not replace your logging in password.
    6. Select Submit, Close and go back to the Slack App and resend the message.
    """)
    email = st.text_input('Enter your Email:', type='default')
    password = st.text_input('Enter your Google App password:', type='password')


    submit_button = st.button('Submit')

    if submit_button:
        if password and email:
            store_app_password(email, password, supabase_client)


if __name__ == "__main__":
    main()
