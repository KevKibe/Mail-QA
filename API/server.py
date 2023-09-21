from supabase import create_client, Client
import json
from openai import OpenAI
from langchain_convo import preprocess_emails
import os
from dotenv import load_dotenv
load_dotenv('.env')
# Initialize our Supabase client
supabase_client = create_client("https://pedailrbwlfhsiwhwued.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBlZGFpbHJid2xmaHNpd2h3dWVkIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODI0NTI2MTQsImV4cCI6MTk5ODAyODYxNH0.8rQquv5lw7WGtxclk8OXr69DbqnxihWumH003GzSvwQ")

# generateEmbeddings
async def generate_embeddings():
    # Initialize OpenAI API
    api_key = os.getenv('OPENAI_API_KEY')
    openai = OpenAI(api_key=api_key)
    
    # Create some custom data (Cooper Codes)
    data = preprocess_emails()
    # documents = [
    #     "Cooper Codes is a YouTuber with 5,300 subscribers",
    #     "Cooper Codes has a website called coopercodes.com",
    #     "Cooper Codes likes clam chowder",
    #     "Cooper Codes has a video covering how to create a custom chatbot with Supabase and OpenAI API"
    # ]

    for dat in data:
        input_text = dat.replace('\n', '')

        # Turn each string (custom data) into an embedding
        embedding_response = openai.create_embedding(
            model="text-embedding-ada-002", # Model that creates our embeddings
            input=input_text
        )

        embedding = embedding_response['data'][0]['embedding']

        # Store the embedding and the text in our supabase DB
        await supabase_client.from_('documents').insert({
            'content': data,
            'embedding': embedding
        })

async def ask_question():
    response = await supabase_client.functions.invoke('ask-custom-data', {
        'body': json.stringify({ 'query': "Is tehre an email on MAachine Learning?" }),
      })
    data = response['data']
    error = response['error']
    print(data)
    print(error)

ask_question()


