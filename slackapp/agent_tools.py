import os
import boto3
import ssl
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from langchain.tools import BaseTool

load_dotenv()


class DataFetchingTool(BaseTool):
    name = "Company Data Fetcher"
    description = '''
                  The Company Data Fetcher is a powerful tool designed to retrieve data from the workspace, including private or company-specific data. With this tool, you can seamlessly access and fetch data stored within the workspace environment. 
                  It provides a secure and efficient way to retrieve data, ensuring the confidentiality and integrity of sensitive information. Whether you need to extract text files, documents, or other data types, the Workspace Data Fetcher simplifies the process, allowing you to effortlessly retrieve the desired data for further analysis, processing, or integration with other tools and systems.

                  '''
                        #         The action input for this tool should strictly be
                        # {
                        #     "action": "Company Data Fetcher",
                        #     "action_input": "the action"
                        # }

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
    

class EmailFetchingTool(BaseTool):
    name = "Email Data Fetcher"
    description = '''
                The Email Data Fetcher is a tool specifically designed to retrieve a user's email data, including emails from their inbox. With this tool, agents can seamlessly access and fetch email data stored within the designated environment. 
                It provides a secure and efficient way to retrieve emails, ensuring the privacy and confidentiality of the user's email communications. 
                By using the Email Data Fetcher, agents can effortlessly retrieve email content, such as subject lines, message bodies, and attachments, for further analysis, processing, or integration with other tools and systems.

               '''
                    # The action input for this tool should strictly be
                    #     {
                    #         "action": "Email Data Fetcher",
                    #         "action_input": ""
                    #     }

    def _run(self, query: str):
        s3 = boto3.client('s3')
        try:
            s3.download_file('mailqa-bucket-01', 'emails.txt', "emails.txt")
            print(f"File 'emails.txt' downloaded successfully from 'mailqa-bucket-01'")
            with open('emails.txt', 'r') as file:
                content = file.read()
            return content
        except Exception as e:
            print(f"Error downloading 'emails.txt' from 'mailqa-bucket-01': {e}")

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")

   
class EmailSendingTool(BaseTool):
    name = "Email Sender Tool"
    description = '''Use this tool to send an email on behalf of the user, if told to send data from 
                   somewhere look in the Data Fetcher Tool or the Email Fetcher Tool
                   Do not send an email if it is to @example.com.
                   The action input for this tool should always include the following parameters:
                   - 'to': The email address of the recipient.
                   - 'subject': The subject of the email.
                   - 'body': The body content of the email.
                   '''

    def _run(self, **action_input):
        load_dotenv()
        email_receiver = action_input.get('to')
        subject = action_input.get('subject')
        body = action_input.get('body')
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
    

class EmailSenderApproval:
    def should_check(self, serialized_obj):
        return serialized_obj.get("name") == "Email Sender Tool"

    def approve(self, input_str):
        # Prompt the user to approve the input and return a boolean value
        response = input(f"Do you approve of the following email to be sent? {input_str} (Y/N): ")
        return response.lower() in ["y", "yes"]

