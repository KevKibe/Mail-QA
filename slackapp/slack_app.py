import os
from agent import Agent, EmailSenderApproval
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
from pathlib import Path 
from supabase import create_client
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from user_auth import UserAuth

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = WebClient(token=os.environ["slack_bot_token"])
app = App(token=os.environ["slack_bot_token"])
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase_client = create_client(supabase_url, supabase_key)

user_auth = UserAuth(supabase_client)

@app.event("message")
def handle_message(event, say):
    channel_type = event['channel_type']
    if 'user' in event:
        user_id = event['user']
        message = event['text']

    try:
        result = client.users_info(user=user_id)
        email = result["user"]["profile"]["email"]
    except SlackApiError as e:
        print(f"Error fetching user info: {e}")
        email = "Unknown"
    user_auth.check_email_and_authenticate(email)

    if channel_type == 'im':      
        agent = Agent()
        start_time = time.time()
        user_input = email + " " + message 
        response = agent.run(user_input)
        say(f"{response}")
        end_time = time.time()
        duration = end_time - start_time
        say(f"{duration}")

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["slack_app_token"]).start()
