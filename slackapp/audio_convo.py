import os
from dotenv import load_dotenv
from supabase import create_client
import streamlit as st
from agent import Agent

from transcription import SpeechRecognition
from elevenlabs import generate, play, set_api_key
from user_auth import UserAuth

elevenlabs_api_key = os.getenv('ELLEVEN_LABS_API')
set_api_key(elevenlabs_api_key)
load_dotenv()
supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase_client = create_client(supabase_url, supabase_key)

agent = Agent()
def generate_and_play_audio(text):
    audio = generate(
        text=text,
        voice="Bella",
        model="eleven_monolingual_v1"
    )
    play(audio)




def main():
    st.title("Talk to Mail QA Assistant")
    st.write('''This is a web application to demonstrate the functionalities of the Mail QA Slack app. 
             All features are active apart from fetching workspace data ''')
    speech_recognition = SpeechRecognition()
    # email = st.text_input("Email")
    email = "keviinkibe@gmail.com"
    user_auth = UserAuth(supabase_client)

    speech_input = st.button("Chat with the app using voice")
    text_input = not speech_input  # Determine if we should use text input

    if text_input:
        transcription = st.text_input("Input your Prompt")
    else:
        audio_data = speech_recognition.record_audio()
        transcription = speech_recognition.transcribe_audio(audio_data)

    submit_button = st.button("Submit")

    if email and (submit_button or speech_input):
        user_auth.check_email_and_authenticate(email)
        
        if transcription:
            st.write(f"You want to find out: {transcription}")
            generate_and_play_audio(transcription)

            message = transcription
            user_input = email + " " + message
            response = agent.run(user_input)
            st.write(f"Response: {response}")
            generate_and_play_audio(response)





# def main():

#     st.title("Talk to Mail QA Assistant")
#     st.write('''This is a web application to demonstrate the functionalities of the Mail QA Slack app. 
#        All features are active apart from fetching workspace data ''')
#     speech_recognition = SpeechRecognition()
#     email = st.text_input("Email")
#     user_auth = UserAuth(supabase_client)

#     user_auth.check_email_and_authenticate( email)
#     speech_input = st.button("Chat with the app using voice")
#     st.title("or")

#     if speech_input:
#         audio_data = speech_recognition.record_audio()
#         transcription = speech_recognition.transcribe_audio(audio_data)
#     else:
#         transcription = st.text_input("Input your Prompt")
#         submit_button = st.button("Submit")
#         user_auth.check_email_and_authenticate( email)

#     if transcription and submit_button:
#         st.write(f"You want to find out: {transcription}")
#         generate_and_play_audio(transcription)

#         message = transcription
#         user_input = email + " " + message
#         response = agent.run(user_input)
#         st.write(f"Response: {response}")
#         generate_and_play_audio(response)

if __name__ == "__main__":
    main()
