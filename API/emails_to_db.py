import os
from supabase import create_client
from text_preprocess import TextProcessor
from gmail_fetch import GmailAPI
from dotenv import load_dotenv
import uuid

class EmailProcessor:
    def __init__(self, supabase_url, supabase_key):
        self.supabase_client = create_client(supabase_url, supabase_key)

    def preprocess_emails(self, days=7):
        text_processor = TextProcessor()
        gmail_api = GmailAPI()
        email_data_list = gmail_api.get_emails(days)
        processed_data = []

        for email_data in email_data_list:
            processed_email_data = text_processor.preprocess_email_data(email_data)
            processed_data.append(processed_email_data)

        return processed_data

    def insert_emails_to_db(self, emails, table_name='email_data'):
        data_to_insert = [{'id': i, 'emails': email} for i, email in enumerate(emails)]
        self.supabase_client.table(table_name).upsert(data_to_insert).execute()


if __name__ == "__main__":
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_KEY')

    email_processor = EmailProcessor(supabase_url, supabase_key)
    emails = email_processor.preprocess_emails()
    email_processor.insert_emails_to_db(emails)


