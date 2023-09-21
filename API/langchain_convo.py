

import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from text_preprocess import TextProcessor
from gmail_fetch import GmailAPI
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv('.env')

def preprocess_emails():
    text_processor = TextProcessor()
    gmail_api = GmailAPI()
    email_data_list = gmail_api.get_emails(1)
    # email_content_list = [(email['From'], email['Date'], email['Subject'], email['Body']) for email in email_data_list]
    processed_data = []

    for email_data in email_data_list:
        processed_email_data = text_processor.preprocess_email_data(email_data)
        processed_data.append(str(processed_email_data))

    return processed_data

def process_tuple(data_tuple):
    processed_tuple = ' '.join(data_tuple)
    return processed_tuple


def initialize_embeddings_and_vectorstore(data):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    model_name = 'text-embedding-ada-002'

    embeddings = OpenAIEmbeddings(
        model=model_name,
        openai_api_key=openai_api_key
    )

    # Process each tuple in the data list
    processed_data = []

    for data_tuple in data:
        # Process the tuple here using your data processing logic
        processed_tuple = process_tuple(data_tuple)
        processed_data.append(processed_tuple)

    # Join the processed data into a single string
    joined_text = " ".join(processed_data)

    # Split the joined text into smaller chunks
    chunk_size = 1000
    chunk_overlap = 200
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=chunk_size, chunk_overlap=chunk_overlap, length_function=len)
    text_chunks = text_splitter.split_text(joined_text)
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    # print(f"Number of OpenAI tokens used: {embeddings.tokens_used}")
    return vectorstore

def similarity_search(vectorstore, query):
   return vectorstore.similarity_search(query, k=3)

def initialize_conversation_chain(vectorstore):
    llm = ChatOpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'), model_name='gpt-3.5-turbo', temperature=0.0)

    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever(search_kwargs={'k': 1}))

    return qa


data = preprocess_emails()
vectorstore = initialize_embeddings_and_vectorstore(data)
query = "what do the emails from LinkedIn say?"
# similar_docs = similarity_search(vectorstore, query)
# similar_text = ' '.join(similar_docs)

qa= initialize_conversation_chain(vectorstore)
response = qa.run(query)

# def initialize_conversation_chain(vectorstore):
#     llm = ChatOpenAI(
#         model_name='gpt-3.5-turbo',
#         model_kwargs={'api_key': os.getenv('OPENAI_API_KEY')}
#         )
#     memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

#     conversation_chain = ConversationalRetrievalChain.from_llm(
#         llm=llm,
#         retriever=vectorstore.as_retriever(),
#         memory=memory
#     )

#     return conversation_chain





# data = preprocess_emails()
# print(data)
# print(len(data))
# print(type(data))
# vectorstore = initialize_embeddings_and_vectorstore(data)
# conversation_chain = initialize_conversation_chain(vectorstore)

# while True:
#     user_input = input(">>> ")
#     if user_input == "quit":
#         break
#     else:
#         print(conversation_chain.run(user_input))