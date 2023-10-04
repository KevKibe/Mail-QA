import os
import time
from conversation import ConversationChain
from token_fetch import fetch_access_token



email = "keviinkibe@gmail.com"    
access_token = fetch_access_token(email)
chatbot = ConversationChain(access_token)
user_input = input(">>> ")
response = chatbot.run_chat(user_input)

print(response)
