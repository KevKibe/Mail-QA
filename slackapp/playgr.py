import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from agent_tools import DataFetchingTool
from langchain.schema.messages import HumanMessage, AIMessage


llm = ChatOpenAI(
    openai_api_key="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",
    temperature=0,
    model_name='gpt-3.5-turbo'
)
# initialize conversational memory
conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True,
    message_class=HumanMessage,
)

tools = [DataFetchingTool()]


# initialize agent with tools
agent = initialize_agent(
    agent='chat-conversational-react-description',
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3,
    early_stopping_method='generate',
    memory=conversational_memory,
    return_messages = True
)
response =agent("how much did the company make?") 
print(response['chat_history'])
print(response['output'])