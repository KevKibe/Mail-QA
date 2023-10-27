import os
import boto3
import time
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.callbacks.human import HumanApprovalCallbackHandler
from agent_tools import DataFetchingTool, EmailFetchingTool, EmailSendingTool, CalenderFetchingTool,EventSchedulingTool
load_dotenv()

class EmailSenderApproval:
    def should_check(self, serialized_obj):
        return serialized_obj.get("name") == "Email Sender Tool"

    def approve(self, input_str):
        approval_statement = f"Do you approve of the following actions? {input_str} (Y/N): "
        approval = input(approval_statement)
        return approval.lower() in ["y", "yes"]
                                  
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
        checker = EmailSenderApproval()
        self.callbacks = [HumanApprovalCallbackHandler(should_check=checker.should_check, approve=checker.approve)]
        self.data_fetching_tool = DataFetchingTool()
        self.email_fetching_tool = EmailFetchingTool()
        self.email_sending_tool = EmailSendingTool()
        self.calender_fetching_tool = CalenderFetchingTool()
        self.event_scheduling_tool = EventSchedulingTool()
        self.tools = [self.email_fetching_tool,self.data_fetching_tool, self.email_sending_tool, self.calender_fetching_tool, self.event_scheduling_tool]

        self.sys_msg = """You are an assistant, assisting with email and workspace related information and 
                        based on provided questions and context. 
                        The user is part of a company and you have access to the company's data using the Company Data Fetcher tool and the user's emails using the Email Data Fetcher.
                        You do not send emails to @example.com extensions ask for the specific email or look in the inbox.
                        You are very talkative and do not give short answers
                        If you can't answer a question, request more information.
                        Strictly do not give a response that starts with "The response to your last comment"  
                        After observing that an email has been sent finish the chain.
                        The email address in the question is the user's email address use that in the tools.
                        When a user asks what email they got an a certain day, use the Email Data Fetcher.
                    """

        self.conversational_memory = ConversationBufferWindowMemory(
            memory_key='chat_history',
            k=5,
            return_messages=True
            )
        self.agent = initialize_agent(
            agent = "chat-conversational-react-description",
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

    def get_email(self):
        return self.user_email
    
    def run(self, prompt):
        response = self.agent.run(prompt)
        return response


# if __name__ == "__main__":
#     email = "keviinkibe@gmail.com"
#     chat_assistant = Agent()
#     prompt = input(">>>")
#     start_time = time.time()
#     resp = chat_assistant.run(email + " " +prompt)
#     end_time = time.time()
#     duration = end_time - start_time
#     print(resp)
#     print(duration)