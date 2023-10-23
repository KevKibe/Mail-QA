import os
import boto3
import ssl
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
from langchain.tools import BaseTool
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
import time

load_dotenv()



class DataFetchingTool(BaseTool):
    name = "Workspace Data Fetcher"
    description = ("use this tool to get data from the workspace also referred to as private data or company data")

    def _run(self, query: str):
        s3 = boto3.client('s3')
        try:
            s3.download_file('mailqa-bucket', 'all_texts.txt', "all_texts.txt")
            print(f"File {'all_texts.txt'} downloaded successfully from {'mailqa-bucket'}")
            with open('all_texts.txt', 'r') as file:
                content = file.read()
            return content
        except Exception as e:
            print(f"Error downloading {'all_texts.txt'} from {'mailqa-bucket'}: {e}")

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")

class EmailFetchingTool(BaseTool):
    name = "Email Data Fetcher"
    description = ("use this tool to get a users email data and emails from his inbox")

    def _run(self, query: str):
        s3 = boto3.client('s3')
        try:
            s3.download_file('mailqa-bucket', 'emails.txt', "emails.txt")
            print(f"File 'emails.txt' downloaded successfully from 'mailqa-bucket'")
            with open('emails.txt', 'r') as file:
                content = file.read()
            return content
        except Exception as e:
            print(f"Error downloading 'emails.txt' from 'mailqa-bucket': {e}")

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")
    
class EmailSendingTool(BaseTool):
    name = "Email Sender Tool"
    description = ("Use this tool to send an email on behalf of the user")

    def _run(self, email_receiver, subject,body):
        load_dotenv()
        email_sender = "keviinkibe@gmail.com"
        email_password = os.getenv('email_password')
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        return em 
    
    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")
    

class Agent:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

        self.llm = ChatOpenAI(
            openai_api_key=self.openai_api_key,
            temperature=0,
            model_name='gpt-3.5-turbo'
        )

        self.conversational_memory = ConversationBufferWindowMemory(
            memory_key='chat_history',
            k=5,
            return_messages=True
        )

        self.data_fetching_tool = DataFetchingTool()
        self.email_fetching_tool = EmailFetchingTool()
        self.email_sending_tool = EmailSendingTool()
        self.tools = [self.email_fetching_tool,self.data_fetching_tool, self.email_sending_tool]

        self.sys_msg = """You are an assistant, assisting with email and workspace related information and tasks based on provided questions and context. 
                    The user is part of a company and you have access to the company's data and the user's emails.
                    You are moderately talkative and do not give short answers
                    If you can't answer a question, request more information. 
                    """
        # self.agent = initialize_agent(
        #         self.tools, self.llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION , verbose=True
        #         )

        self.agent = initialize_agent(
            agent='structured-chat-zero-shot-react-description',
            tools=self.tools,
            llm=self.llm,
            verbose=True,
            max_iterations=3,
            early_stopping_method='generate',
            memory=self.conversational_memory
        )
        
        new_prompt = self.agent.agent.create_prompt(
            system_message=self.sys_msg,
            tools=self.tools
        )
        self.agent.agent.llm_chain.prompt = new_prompt

    def run(self, prompt):
        response = self.agent.run(prompt)
        return response


if __name__ == "__main__":
    chat_assistant = Agent()
    prompt = input(">>>")
    resp = chat_assistant.run(prompt)
    print(resp)

