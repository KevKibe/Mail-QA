import os
from pathlib import Path
import boto3
import time
from mail_fetch import GmailAPI
from mail_preprocess import TextProcessor
from supabase import create_client
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
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
        email_data_list = gmail_api.get_emails(1)
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
            with open("emails.txt", "w") as f:
                f.write(txt)
            self.upload_to_s3("emails.txt", "mailqa-bucket")
            time.sleep(90)  # Wait for 90 seconds

email_processor = EmailUploader("keviinkibe@gmail.com")
email_processor.process_emails_continuously()






























# embeddings = OpenAIEmbeddings(
#             model='text-embedding-ada-002',
#             openai_api_key=openai_api_key
#         )

# fs = LocalFileStore("./cache/")

# cached_embedder = CacheBackedEmbeddings.from_bytes_store(
#     embeddings, fs, namespace=embeddings.model
# )


# chunk_size = 1000
# chunk_overlap = 200
# text_splitter = CharacterTextSplitter(separator = '\n', chunk_size=chunk_size, chunk_overlap=chunk_overlap)
# text_chunks = text_splitter.split_text(txt)
# vectorstore = FAISS.from_texts(texts=text_chunks, embedding=cached_embedder)

# llm = ChatOpenAI(
#             model_name='gpt-3.5-turbo',
#             model_kwargs={'api_key': openai_api_key},
#             temperature= 0
#         )
# template = """As an AI assistant, I assist with email and workspace data based on provided questions and context. 
#             Company data refers to non-email knowledge base data shared in a workspace. 
#             If I can't answer a question, I'll request more information. 
#             Question: {question} {context}
#             Answer:"""
# prompt_template = PromptTemplate(input_variables=["question", "context"], template=template) 
# memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
# conversation_chain = RetrievalQA.from_chain_type(
#             llm=llm,
#             # chain_type_kwargs={"prompt": prompt_template},
#             memory=memory,
#             retriever=vectorstore.as_retriever()
#         )


# prompt = input(">>>")
# start_time = time.time()
# response = conversation_chain.run(prompt)
# end_time = time.time()
# duration = end_time - start_time
# print(response)
# print(duration)