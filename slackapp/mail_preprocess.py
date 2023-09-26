import re
from bs4 import BeautifulSoup

def preprocess_text(text):
    text = text.replace('\u200c', '').replace('\u034f', '').replace('\ufeff', '').replace("\\u00a9",'')
    text = re.sub(r'\s+', ' ', text)
    return text

class TextProcessor:
    def __init__(self):
        self.url_pattern = re.compile(r'https?://\S+|www\.\S+')

    def remove_html_tags(self, text):
        """Removes all HTML tags from the text"""
        soup = BeautifulSoup(text, 'html.parser')
        return soup.get_text()

    def remove_links(self, text):
        """Replaces URLs with an empty string"""
        text_without_links = self.url_pattern.sub('', text)
        return text_without_links

    def preprocess_email_data(self, email_data):
        email = email_data[0]
        preprocessed_body = self.remove_html_tags(email['Body'])
        preprocessed_body = self.remove_links(preprocessed_body)

        processed_email_data = {
            'From': email['From'],
            'Date': email['Date'],
            'Subject': email['Subject'],
            'Labels': email.get('Labels', []),  
            'Body': preprocess_text(preprocessed_body),  
        }
        return processed_email_data




# text_processor = TextProcessor()
# gmail_api = GmailAPI()
# emails = gmail_api.get_emails(5)

# processed_email_data_list = []

# for email_data in emails:
#     processed_email_data = text_processor.preprocess_email_data(email_data)
#     processed_email_data_list.append(processed_email_data)
# # print(type(processed_email_data_list))
# print(processed_email_data_list)
# Display the processed email data
# for processed_email_data in processed_email_data_list:
#     print(processed_email_data)
#     print(type(processed_email_data))