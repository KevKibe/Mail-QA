import os
from dotenv import load_dotenv
from pathlib import Path 
from supabase import create_client


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase_client = create_client(supabase_url, supabase_key)


def fetch_access_token(email):
    """Fetches the access token from the Supabase database."""
    try:
        access_token = supabase_client.table('slack_app').select('accesstoken').eq('email', email).single().execute()
        return access_token.data['accesstoken']
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None