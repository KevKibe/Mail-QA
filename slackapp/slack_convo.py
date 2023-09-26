import os
from mail_fetch import GmailAPI
from mail_preprocess import TextProcessor
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

class ConversationChain:
    def __init__(self):
        load_dotenv()
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def preprocess_emails(self):
        text_processor = TextProcessor()
        gmail_api = GmailAPI()
        email_data_list = gmail_api.get_emails(5)
        # email_content_list = [(email['From'], email['Date'], email['Subject'], email['Body']) for email in email_data_list]
        processed_data = []

        for email_data in email_data_list:
            processed_email_data = text_processor.preprocess_email_data(email_data)
            processed_data.append(str(processed_email_data))

        return processed_data

    def initialize_embeddings_and_vectorstore(self, data):
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
            text_chunks = text_splitter.split_text(item)
            all_text_chunks.extend(text_chunks)

        vectorstore = FAISS.from_texts(texts=all_text_chunks, embedding=embeddings)
        return vectorstore

    def initialize_conversation_chain(self, vectorstore):
        llm = ChatOpenAI(
            model_name='gpt-3.5-turbo',
            model_kwargs={'api_key': self.openai_api_key}
        )
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
        conversation_chain = RetrievalQA.from_chain_type(
            llm=llm,
            memory=memory,
            retriever=vectorstore.as_retriever()
        )
        return conversation_chain

    def run_chat(self, user_input):
        emails = self.preprocess_emails()
        vectorstore = self.initialize_embeddings_and_vectorstore(emails)
        conversation_chain = self.initialize_conversation_chain(vectorstore)

        return conversation_chain.run(user_input)
    
# if __name__ == "__main__":
#     chat_bot = ConversationChain()
#     user_input = input(">>> ")
#     response = chat_bot.run_chat(user_input)
#     print(response)