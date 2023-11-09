from langchain.callbacks.human import HumanApprovalCallbackHandler
from langchain.tools import BaseTool
import boto3
import os
from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent

openai_api_key = os.getenv('OPENAI_API_KEY')

def should_check(serialized_obj: dict) -> bool:
    # Only require approval on ShellTool.
    return serialized_obj.get("name") == "Email Sender Tool"

def approve(self, input_str):
        approval_statement = f"Do you approve of the following actions? {input_str} (Y/N): "
        approval = input(approval_statement)
        return approval.lower() in ["y", "yes"]

callbacks = [HumanApprovalCallbackHandler(should_check=should_check, approve=approve)]


class DataFetchingTool(BaseTool):
    name = "Company Data Fetcher"
    description = '''
                  The Company Data Fetcher is a powerful tool designed to retrieve data from the workspace, including private or company-specific data. With this tool, you can seamlessly access and fetch data stored within the workspace environment. 
                  It provides a secure and efficient way to retrieve data, ensuring the confidentiality and integrity of sensitive information. Whether you need to extract text files, documents, or other data types, the Workspace Data Fetcher simplifies the process, allowing you to effortlessly retrieve the desired data for further analysis, processing, or integration with other tools and systems.
                  If there is no company data related to the query say that there is no data related to the question and ask for more information.
                  The action input for this tool should strictly be a string.
                  '''
    def _run(self, query: str):
        s3 = boto3.client('s3')
        try:
            s3.download_file('mailqa-bucket-01', 'all_texts.txt', "all_texts.txt")
            print(f"File {'all_texts.txt'} downloaded successfully from {'mailqa-bucket-01'}")
            with open('all_texts.txt', 'r') as file:
                content = file.read()
            return content
        except Exception as e:
            print(f"Error downloading {'all_texts.txt'} from {'mailqa-bucket-01'}: {e}")

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")
    
llm = ChatOpenAI(
            openai_api_key=openai_api_key,
            temperature=0,
            model_name='gpt-3.5-turbo'
        )
tools = [DataFetchingTool()]
agent = initialize_agent(
            agent = "chat-conversational-react-description",
            tools=tools,
            llm=llm,
            verbose=True,
            max_iterations=3,
            early_stopping_method='generate',
        )

prompt = input(">>>")
response = agent.run(prompt)