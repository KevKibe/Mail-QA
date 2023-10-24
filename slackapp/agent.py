import os
import boto3
import time
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.callbacks.human import HumanApprovalCallbackHandler
from agent_tools import DataFetchingTool, EmailFetchingTool, EmailSenderApproval, EmailSendingTool
import time

load_dotenv()


                                  
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
        callbacks = [HumanApprovalCallbackHandler(should_check=checker.should_check, approve=checker.approve)]
        self.data_fetching_tool = DataFetchingTool()
        self.email_fetching_tool = EmailFetchingTool()
        self.email_sending_tool = EmailSendingTool(callbacks=callbacks)
        self.tools = [self.email_fetching_tool,self.data_fetching_tool, self.email_sending_tool]

        self.sys_msg = """You are an assistant, assisting with email and workspace related information and 
                        based on provided questions and context. 
                        The user is part of a company and you have access to the company's data using the Company Data Fetcher tool and the user's emails using the Email Data Fetcher.
                        You do not send emails to @example.com extensions ask for the specific email or look in the inbox.
                        You are very talkative and do not give short answers
                        If you can't answer a question, request more information. 

                    """
                        # Strictly use this input for Company Data Fetcher tool and Email Data Fetcher tool
                        # {
                        #     "action": "Tool",
                        #     "action_input": "the action"
                        # }
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

    def run(self, prompt):
        response = self.agent.run(prompt)
        return response


# if __name__ == "__main__":
#     chat_assistant = Agent()
#     prompt = input(">>>")
#     start_time = time.time()
#     resp = chat_assistant.run(prompt)
#     end_time = time.time()
#     duration = end_time - start_time
#     print(resp)
#     print(duration)