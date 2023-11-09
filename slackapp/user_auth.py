import os
from dotenv import load_dotenv
from pathlib import Path 
from supabase import create_client
from auth import authenticate


class UserAuth:
    def __init__(self, supabase_client):
        self.supabase_client = supabase_client

    def store_email_accesstoken(self, email, access_token):
        """Stores the email and access token in the Supabase database."""
        try:
            data_to_insert = [{'email': email, 'accesstoken': access_token}]
            self.supabase_client.table('slack_app').upsert(data_to_insert).execute()
            print("Data inserted successfully.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def fetch_access_token(self, email):
        """Fetches the access token from the Supabase database."""
        try:
            access_token = self.supabase_client.table('slack_app').select('accesstoken').eq('email', email).single().execute()
            return access_token.data['accesstoken']
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def check_email_and_authenticate(self, email):
        """Checks if the email exists in the 'email' table and authenticates user if it doesn't."""
        try:
            result = self.supabase_client.table('slack_app').select('email').eq('email', email).execute()
            if not result.data:
                access_token = authenticate()
                self.store_email_accesstoken(email, access_token)
            else: 
                print("Email found in the table.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")