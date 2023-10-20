import os
import requests
import string
from slack import WebClient
from slack.errors import SlackApiError
from dotenv import load_dotenv
from text_extractor import TextExtractor

load_dotenv()

class SlackFileRetriever:
    def __init__(self, token=None):
        """
        Initializes a SlackFileManager instance.

        Args:
            token (str): The Slack API token.
        """
        self.token = token if token else os.getenv("slack_bot_token")

    def get_file_list(self):
        """
        Retrieves a list of files from Slack channels.

        Returns:
            list: A list of dictionaries containing file information.
        """
        file_list = []
        try:
            client = WebClient(token=self.token)
            channels = client.conversations_list(exclude_archived=True)["channels"]
            for channel in channels:
                channel_id = channel["id"]
                channel_name = channel["name"]
                response = client.files_list(channel=channel_id)
                files = response["files"]
                if files:
                    for file in files:
                        if 'download/canvas' not in file["url_private_download"]:
                           file_info = {
                            "file_id":file['id'],     
                            "channel_name": channel_name,
                            "file_name": file["name"],
                            "file_url": file["url_private_download"]
                        }
                           file_list.append(file_info)
        except SlackApiError as e:
            if e.response['error'] != 'not_in_channel':
                print(f"Error: {e.response['error']}")
        return file_list

    @staticmethod
    def preprocess(text):
        """
        Preprocesses text by removing spaces, punctuation marks, and converting to lowercase.

        Args:
            text (str): The input text to be preprocessed.

        Returns:
            str: The preprocessed text.
        """
        # text = text.replace(" ", "")
        text = text.translate(str.maketrans("", "", string.punctuation))
        text = text.lower()
        return text

    def download_extract_text_remove(self, file_info):
        """
        Downloads a file, extracts text, preprocesses it, and removes the temporary file.

        Args:
            file_info (dict): A dictionary containing file information.

        Returns:
            None
        """
        file_id = file_info["file_id"]
        file_name = file_info['file_name']
        file_url = file_info['file_url']
        response = requests.get(file_url, headers={"Authorization": f"Bearer {self.token}"})
        if response.status_code == 200:
            with open(file_name, "wb") as temp_file:
                temp_file.write(response.content)
            text_extractor = TextExtractor(file_name)
            extracted_text = text_extractor.extract_text()
            extracted_text = self.preprocess(extracted_text)
            return extracted_text
        else:
            print(f"Failed to download: {file_name}")

