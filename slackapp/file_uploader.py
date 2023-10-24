import boto3
from slack import WebClient
from slack.errors import SlackApiError
import time
import os
from dotenv import load_dotenv
from file_extractor import SlackFileRetriever

load_dotenv()


class SlackFileUploader:
    def __init__(self, token):
        self.token = token
        self.slack_file_retriever = SlackFileRetriever()
        self.checked_files = set()  
    
    def upload_to_s3(self, file_name, bucket_name):
        """
        Uploads a file to an AWS S3 bucket.

        """
        s3 = boto3.client('s3')
        try:
            s3.upload_file(file_name, bucket_name, file_name)
            print(f"File {file_name} uploaded successfully to {bucket_name}")
        except Exception as e:
            print(f"Error uploading {file_name} to {bucket_name}: {e}")

    def convert_to_paragraph(self,file_path):
        """
        Converts a text file with each word on a new line to paragraph style.

        Args:
            file_path (str): The path to the text file.

        Returns:
            str: The paragraph style text.
        """
        with open(file_path, 'r') as file:
            lines = file.readlines()
            paragraph = ' '.join(line.strip() for line in lines)
        return paragraph

    def check_uploaded_files(self):
        all_texts = ""
        while True:
            file_list = self.slack_file_retriever.get_file_list()
            if file_list:
                for file_info in file_list:
                    file_id = file_info["file_id"]
                    if file_id not in self.checked_files:
                        self.checked_files.add(file_id)  # Mark as checked
                        channel_name = file_info["channel_name"]
                        file_name = file_info["file_name"]
                        file_url = file_info["file_url"]
                        print(f"New file added! Channel: {channel_name}, File Name: {file_name}, File URL: {file_url}")
                        
                        extracted_text = self.slack_file_retriever.download_extract_text_remove(file_info)
                        all_texts += f"File Name: {file_name}\n" + extracted_text +"\n"
                        with open("all_texts.txt","w") as text_file:
                            text_file.write(all_texts)
                        paragraph_text = self.convert_to_paragraph("all_texts.txt")
                        with open("all_texts.txt","w") as text_file:
                            text_file.write(paragraph_text)

                        self.upload_to_s3("all_texts.txt", "mailqa-bucket-01")
            time.sleep(1)  


slack_checker = SlackFileUploader(token=os.getenv("slack_bot_token"))
slack_checker.check_uploaded_files()
