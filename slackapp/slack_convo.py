import os
import boto3
from mail_fetch import GmailAPI
from langchain.vectorstores import Chroma
from langchain.storage import LocalFileStore
from langchain.embeddings import CacheBackedEmbeddings
from mail_preprocess import TextProcessor
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts.prompt import PromptTemplate
from file_extractor import SlackFileRetriever

class ConversationChain:
    def __init__(self, access_token):
        load_dotenv()
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.access_token = access_token

    # def preprocess_emails(self):
    #     """Fetching and preprocesses the emails."""
    #     text_processor = TextProcessor()
    #     gmail_api = GmailAPI(self.access_token)
    #     email_data_list = gmail_api.get_emails(1)
    #     processed_data = []

    #     for email_data in email_data_list:
    #         processed_email_data = text_processor.preprocess_email_data(email_data)
    #         processed_data.append(str(processed_email_data))

    #     return processed_data
    
    def read_file_from_s3(self,file_name, bucket_name):
        """
        Downloads a file from an AWS S3 bucket and reads its content.

        Args:
            file_name (str): The name of the file to download.
            bucket_name (str): The name of the S3 bucket.

        Returns:
            str: The content of the file.
        """
        s3 = boto3.client('s3')
        try:
            s3.download_file(bucket_name, file_name, file_name)
            print(f"File {file_name} downloaded successfully from {bucket_name}")
            with open(file_name, 'r') as file:
                content = file.read()
            return content
        except Exception as e:
            print(f"Error downloading {file_name} from {bucket_name}: {e}")

    def join_data(self):
        slack_file_data = self.read_file_from_s3("all_texts.txt","mailqa-bucket") 
        user_email_data = self.read_file_from_s3("emails.txt","mailqa-bucket")
        data = slack_file_data + user_email_data 
        return data
        

    def initialize_embeddings_and_vectorstore(self, data):
        """Initializes the embeddings and vectorstore for the chatbot."""
        model_name = 'text-embedding-ada-002'

        embeddings = OpenAIEmbeddings(
            model=model_name,
            openai_api_key=self.openai_api_key
        )
        fs = LocalFileStore("./cache/")

        cached_embedder = CacheBackedEmbeddings.from_bytes_store(embeddings, fs, namespace=embeddings.model)
                                                                

        chunk_size = 1000
        chunk_overlap = 200
        text_splitter = CharacterTextSplitter(separator="\n", chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        text_chunks = text_splitter.split_text(data)
        vectorstore = FAISS.from_texts(texts=text_chunks, embedding=cached_embedder)
        return vectorstore

    def initialize_conversation_chain(self, vectorstore):
        """Initializes the conversation chain for the chatbot."""
        llm = ChatOpenAI(
            model_name='gpt-3.5-turbo',
            model_kwargs={'api_key': self.openai_api_key},
            temperature= 0
        )
        template = """As an AI assistant, I assist with email and workspace data based on provided questions and context. 
                    Company data after a filename and emails are those with tags from, date, subject, labels. 
                    If I can't answer a question, I'll request more information. 
                    Question: {question} {context}
                    Answer:"""
        prompt_template = PromptTemplate(input_variables=["question", "context"], template=template) 
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
        conversation_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type_kwargs={"prompt": prompt_template},
            memory=memory,
            retriever=vectorstore.as_retriever()
        )
        return conversation_chain

    def run_chat(self, user_input):
        """Runs the chatbot."""
        data = self.join_data()
        vectorstore = self.initialize_embeddings_and_vectorstore(data)
        conversation_chain = self.initialize_conversation_chain(vectorstore)

        return conversation_chain.run(user_input)
        # return data
        
