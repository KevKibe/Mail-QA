import os
from mail_fetch import GmailAPI
from langchain.vectorstores import Chroma
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

    def preprocess_emails(self):
        """Fetching and preprocesses the emails."""
        text_processor = TextProcessor()
        gmail_api = GmailAPI(self.access_token)
        email_data_list = gmail_api.get_emails(5)
        processed_data = []

        for email_data in email_data_list:
            processed_email_data = text_processor.preprocess_email_data(email_data)
            processed_data.append(str(processed_email_data))

        return processed_data
    
    def join_data(self,email_data):
        slack_file_retriever = SlackFileRetriever()
        file_list = slack_file_retriever.get_file_list()
        file_data = []
        for file_info in file_list:
            extracted_data = slack_file_retriever.download_extract_text_remove(file_info)
            file_data.append(extracted_data)
        
        data = [item for item in email_data if item is not None]+file_data
        return data
        

    def initialize_embeddings_and_vectorstore(self, data):
        """Initializes the embeddings and vectorstore for the chatbot."""
        model_name = 'text-embedding-ada-002'

        embeddings = OpenAIEmbeddings(
            model=model_name,
            openai_api_key=self.openai_api_key
        )

        chunk_size = 1000
        chunk_overlap = 200
        text_splitter = CharacterTextSplitter(separator="\n", chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len)

        all_text_chunks = []

        for item in data:
            if item is not None and isinstance(item, str):
                text_chunks = text_splitter.split_text(item)
                all_text_chunks.extend(text_chunks)
            else:
                print(f"Skipping invalid input: {item}")

        vectorstore = FAISS.from_texts(texts=all_text_chunks, embedding=embeddings)
        return vectorstore

    def initialize_conversation_chain(self, vectorstore):
        """Initializes the conversation chain for the chatbot."""
        llm = ChatOpenAI(
            model_name='gpt-3.5-turbo',
            model_kwargs={'api_key': self.openai_api_key},
            temperature= 0
        )
        template = """You are an AI assistant that helps with email data and workspace data given a question and context as worksapace data and emails.
                      Any mention of company data is data in the knowledge base that is not related to emails and it is shared in a workspace environment.
                      The AI is talkative and descriptive. 
                      If the AI does not know the answer to a question,ask to provide more information about question. 
                      Question: {question} {context}
                      Answer:"""
        prompt = PromptTemplate(input_variables=["question", "context"], template=template) 
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
        conversation_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type_kwargs={"prompt": prompt},
            memory=memory,
            retriever=vectorstore.as_retriever()
        )
        return conversation_chain

    def run_chat(self, user_input):
        """Runs the chatbot."""
        emails = self.preprocess_emails()
        data = self.join_data(emails)
        vectorstore = self.initialize_embeddings_and_vectorstore(data)
        conversation_chain = self.initialize_conversation_chain(vectorstore)

        return conversation_chain.run(user_input)
        
