import os
from pathlib import Path
import boto3
import time
from mail_fetch import GmailAPI
from mail_preprocess import TextProcessor
from supabase import create_client
from dotenv import load_dotenv
load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase_client = create_client(supabase_url, supabase_key)


class EmailUploader:
    def __init__(self, email):
        self.email = email
        self.access_token = self.fetch_access_token(email)

    def fetch_access_token(self, email):
        """Fetches the access token from the Supabase database."""
        try:
            access_token = supabase_client.table('slack_app').select('accesstoken').eq('email', email).single().execute()
            return access_token.data['accesstoken']
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def preprocess_emails(self):
        """Fetching and preprocesses the emails."""
        text_processor = TextProcessor()
        gmail_api = GmailAPI(self.access_token)
        email_data_list = gmail_api.get_emails(7)
        processed_data = []

        for email_data in email_data_list:
            processed_email_data = text_processor.preprocess_email_data(email_data)
            processed_data.append(str(processed_email_data))
        
        data = ' '.join(processed_data)
        return data
    
    def upload_to_s3(self, file_name, bucket_name):
        """
        Uploads a file to an AWS S3 bucket.
        """
        s3 = boto3.client('s3')
        try:
            s3.upload_file(file_name, bucket_name, file_name)
            print(f"File {file_name} uploaded successfully to {bucket_name}")
        except Exception as e:
            print(f"Error uploading {file_name} to {bucket_name}: {e}")

    def process_emails_continuously(self):
        while True:
            txt = self.preprocess_emails()
            with open(f"{self.email}_emails.txt", "w") as f:
                f.write(txt)
            self.upload_to_s3(f"{self.email}_emails.txt", "mailqa-bucket-01")
            time.sleep(5)  

email_processor = EmailUploader("keviinkibe@gmail.com")
email_processor.process_emails_continuously()