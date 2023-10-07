import os
import time
# from conversation import ConversationChain
from token_fetch import fetch_access_token
from gmail_fetch import GmailAPI
from text_preprocess import TextProcessor
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.graphs import Neo4jGraph
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
username = os.getenv('neo4j_username')
url = os.getenv('neo4j_url')
username = os.getenv('neo4j_username')
password = os.getenv('neo4j_password')


# print(openai_api_key)


def preprocess_emails(access_token):
    """Fetching and preprocesses the emails."""
    text_processor = TextProcessor()
    gmail_api = GmailAPI(access_token)
    email_data_list = gmail_api.get_emails(1)
    processed_data = []

    for email_data in email_data_list:
        processed_email_data = text_processor.preprocess_email_data(email_data)
        processed_data.append(str(processed_email_data))

    return processed_data

graph = Neo4jGraph(
    url=url, username=username, password=password
)
print(graph)

# vector_index = Neo4jVector.from_existing_graph(
#     OpenAIEmbeddings(),
#     url=url,
#     username=username,
#     password=password,
#     index_name='tasks',
#     node_label="Task",
#     text_node_properties=['name', 'description', 'status'],
#     embedding_node_property='embedding',
# )


# email = "keviinkibe@gmail.com"    
# access_token = fetch_access_token(email)
# emails = preprocess_emails(access_token)
# print(emails)