import os
from slack_convo import ConversationChain
from agent import Agent
import time
from auth import authenticate
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
from pathlib import Path 
from supabase import create_client
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = WebClient(token=os.environ["slack_bot_token"])
app = App(token=os.environ["slack_bot_token"])

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase_client = create_client(supabase_url, supabase_key)


def store_email_accesstoken(email, access_token, supabase_client):
    """Stores the email and access token in the Supabase database."""
    try:
        data_to_insert = [{'email': email, 'accesstoken': access_token}]
        supabase_client.table('slack_app').upsert(data_to_insert).execute()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def fetch_access_token(email):
    """Fetches the access token from the Supabase database."""
    try:
        access_token = supabase_client.table('slack_app').select('accesstoken').eq('email', email).single().execute()
        return access_token.data['accesstoken']
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    

def check_email_and_authenticate(email, supabase_client):
    """Checks if the email exists in the 'email' table and authenticates user if it doesn't."""
    try:
        result = supabase_client.table('slack_app').select('email').eq('email', email).execute()
        if not result.data:
            access_token = authenticate()
            store_email_accesstoken(email, access_token, supabase_client)
        else:
            print("Email found in the table.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")



@app.event("message")
def handle_message(event, say):
    channel_type = event['channel_type']
    user_id = event['user']
    message = event['text']

    # Fetch user info
    try:
        result = client.users_info(user=user_id)
        email = result["user"]["profile"]["email"]
    except SlackApiError as e:
        print(f"Error fetching user info: {e}")
        email = "Unknown"
    check_email_and_authenticate(email, supabase_client)

    if channel_type == 'im':      
        # access_token = fetch_access_token(email)
        
        # chatbot = ConversationChain(access_token)
        agent = Agent()
        start_time = time.time()
        user_input = message
        response = agent.run(user_input) 
        say(f"{response}")
        end_time = time.time()
        duration = end_time - start_time
        print(duration)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["slack_app_token"]).start()
