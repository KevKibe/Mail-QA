import os
import boto3
import ssl
import json
import datetime
import smtplib
import pytz
from email.message import EmailMessage
from mail_fetch import GmailAPI
from mail_preprocess import TextProcessor
from pydantic import BaseModel
from datetime import timedelta
from dotenv import load_dotenv
from langchain.tools import BaseTool
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from supabase import create_client
load_dotenv()

nairobi = pytz.timezone('Africa/Nairobi')
nairobi_time = datetime.datetime.now(nairobi)



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
    



class EmailFetchingTool(BaseTool):
    name = "Email Data Fetcher"
    description = f'''
                The Email Data Fetcher is a tool specifically designed to retrieve a user's email data, including emails from their inbox. 
                Today's date and time is {nairobi_time}.
                What is returned is updated recent emails in my inbox so you have access to my emails.
                When asked for emails in the inbox give a summary of the emails and their content.
                When asked about a specific email return every information about the email, if there is no email related to the query say that there is no email related to the question and ask for more information.
                The action input for this tool should always include the following parameters:
                  - 'user_email': The user's email address that is in the prompt.
               '''
    def _run(self, **action_input):
        email = action_input.get('user_email')
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_KEY')
        supabase_client = create_client(supabase_url, supabase_key)
        access_token = supabase_client.table('slack_app').select('accesstoken').eq('email', email).single().execute()
        access_token = access_token.data['accesstoken']
        
        text_processor = TextProcessor()
        gmail_api = GmailAPI(access_token)
        email_data_list = gmail_api.get_emails(7)
        processed_data = []
        for email_data in email_data_list:
            processed_email_data = text_processor.preprocess_email_data(email_data)
            processed_data.append(str(processed_email_data))
        data = ' '.join(processed_data)
        return data
    
    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")


    
class EmailSendingTool(BaseTool):
    name = "Email Sender Tool"
    description  = '''Use this tool to send an email on behalf of the user, if told to send data from 
                   somewhere look in the Data Fetcher Tool or the Email Fetcher Tool
                   Do not send an email if it is to @example.com.
                   Strictly The action input for this tool should always include the following parameters:
                   - 'email_sender': str - The user's email address that is the email address in the prompt always.
                   - 'to': str - The email address of the recipient always.
                   - 'subject': str - The subject of the email always.
                   - 'body': str - The body content of the email always.
                   
                   End the email with just the words 'Best Regards' and space it accordingly. 
                   After using the tool say return a confirmation of the email sending, eho its been sent to and the content of the email.
                   Finish the chain after observing that the email(s) has been sent.
                   Return the content of only that one email sent not more than that one.
                   Strictly do not execute the Email Data Fetcher tool after using this tool just finish the chain.
                   Avoid saying 'The response to your last comment is:', replace with the content of the email sent...
                   '''

    def _run(self,**action_input):
        load_dotenv()
        email_receiver = action_input.get('to')
        subject = action_input.get('subject')
        body = action_input.get('body')
        email_sender = action_input.get('email_sender')
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

class CalenderFetchingTool(BaseTool):
    name = "Calender Events Fetcher"
    description = '''
                  The Calender Events Fetcher is a powerful tool designed to retrieve calender events in the user's calender. 
                  The action input for this tool should always include the following parameters:
                  - 'user_email': The user's email address that is in the prompt.
                  Respond with the events and the links to the events
                  ''' 
    def _run(self, **action_input):
       email = action_input.get('user_email')
       supabase_url = os.getenv('SUPABASE_URL')
       supabase_key = os.getenv('SUPABASE_KEY')
       supabase_client = create_client(supabase_url, supabase_key)
       max_results = 10
       access_token = supabase_client.table('slack_app').select('accesstoken').eq('email', email).single().execute()
       access_token_data = access_token.data  
       token_data = json.loads(access_token_data['accesstoken'])
       credentials = Credentials.from_authorized_user_info(token_data)
       service = build('calendar', 'v3', credentials=credentials)
       nairobi = pytz.timezone('Africa/Nairobi')
       now = datetime.datetime.now(nairobi)
       now = now.isoformat()
       events_list = []
       try:
           events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=max_results, singleEvents=True,
                                        orderBy='startTime').execute()
           events = events_result.get('items', [])

           if not events:
               return 'No upcoming events found.'
           else:
               for event in events:
                   start = event['start'].get('dateTime', event['start'].get('date'))
                   summary = event['summary']
                   link = event['htmlLink']  
                   events_list.append((summary, start,link))  
                
           return events_list
       except Exception as error:
           return f'An error occurred: {error}'



class EventSchedulingTool(BaseTool):
    name = "Calender Event Scheduler"
    description = f'''
                  The Calender Events Scheduler is a powerful tool designed to schedule calender events in the user's calender. 
                  Today's date and time is {nairobi_time}.
                  Strictly the action input for this tool should always include the following parameters:
                   - 'summary': str - The summary of the event.
                   - 'year': int - The year of the start time of the event.Default is 2023.
                   - 'month': int - The month the event is to start .
                   - 'day': int - The day the event is to start.
                   - 'hour': int - The hour the event is to start.
                   - 'duration': int - How long the event is to take in hours, default is 1 hr. 
                   - 'attendees': str - Emails of attendees of the event created. If is is not specified send an empty list. Make it a list if there is more than one attendee. 
                   - 'user_email':str - The user's email address that is in the prompt.
                  '''
    def _run(self, **action_input):
       summary = action_input.get('summary')
       year = action_input.get('year')
       month = action_input.get('month')
       day = action_input.get('day')
       hour = action_input.get('hour')
       duration = action_input.get('duration')
       attendees = action_input.get('attendees')
       email = action_input.get('user_email')
       start_time = datetime.datetime(year = year, month = month, day = day, hour = hour)
       end_time = start_time + timedelta(hours = duration)
       supabase_url = os.getenv('SUPABASE_URL')
       supabase_key = os.getenv('SUPABASE_KEY')
       supabase_client = create_client(supabase_url, supabase_key)
       access_token = supabase_client.table('slack_app').select('accesstoken').eq('email', email).single().execute()
       access_token_data = access_token.data  # Extract the JSON data
       token_data = json.loads(access_token_data['accesstoken'])
       credentials = Credentials.from_authorized_user_info(token_data)
       service = build('calendar', 'v3', credentials=credentials)
       event = {
           'summary': summary,
           'start': {
               'dateTime': start_time.isoformat(),
               'timeZone': 'Africa/Nairobi',
           },
           'end': {
               'dateTime': end_time.isoformat(),
               'timeZone': 'Africa/Nairobi',
           },
        'attendees': [{'email': attendee} for attendee in attendees],
       }
       event = service.events().insert(calendarId='primary', body=event).execute()
    #    return print(f"Event created: {event['htmlLink']}")
       return event['htmlLink']

    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")
