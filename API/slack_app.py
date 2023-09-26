import os
from conversation import ConversationChain 
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
from pathlib import Path 
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Create a client instance for fetching user info
client = WebClient(token=os.environ["slack_bot_token"])

app = App(token=os.environ["slack_bot_token"])
chatbot = ConversationChain()
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

    # print(f"Message: {message}, Email: {email}")

    if channel_type == 'im':
        user_input = message
        response = chatbot.run_chat(user_input) 
        # Handle message sent to inbox
        say(f"{response}")

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["slack_app_token"]).start()
