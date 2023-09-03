# Mail-QA
Mail QA is a chat-based web application that is focused on addressing the issue of professionals spending a significant portion of their workday on email communication. 
The proposed solution involves using generative AI to streamline email management and improve productivity.<br>
This repository contains the source code and development history of the Mail QA platform.

## How we are Solving the Problem
The proposed solution involves using generative AI specifically OpenAI models to streamline email management
and improve productivity. Here's a breakdown of the key components:
- Understand the content of emails, including text extraction, language processing,
and context comprehension.
- Allow users to interact with the AI using natural language prompts and be
capable of interpreting these prompts to perform actions like summarizing emails,
searching for specific information, or generating responses..
- Generate concise summaries of emails based on user requests for example
extracting key points, identifying important information, and presenting it in a
user-friendly format.
- Understand the context of an email and generate appropriate and coherent
responses quickly and appropriately.
- Support 98 languages as currently supported by the OpenAI API ensuring that
users from diverse linguistic backgrounds can benefit from the AI-powered email
management and communication features.
- Have an intuitive user interface that allows users to input prompts, view
summaries, and access generated responses

## Structure
```sh
├── Mail-QA/

│ ├── API/
│ │ ├── api.py - API server to receive and respond to request for the chatbot.
│ │ ├── app.py - chat-interface.
│ │ ├── auth.py - OAuth and Authorization for the API.
│ │ ├── gmail_fetch.py - fetching user's email data.
│ │ ├── langchain_convo.py - initializing the conversation chain using langchain and OpenAI API.
│ │ ├── requirements.txt - libraries and dependencies for the API.
│ │ ├── text_preprocess.py - processing email data.
│ │ ├── token.pickle - storing tokens from OAuth.

│ ├── UI/
│ │ ├── index.html - UI design for homepage
│ │ ├── signup/
  │ │ ├── index.html - signup page
│ │ ├── login/
  │ │ ├── index.html - login page
│ │ ├── prompt/
  │ │ ├── index.html - prompt page
│ │ ├── assets/
  │ │ ├── css/
    │ │ ├── _root.scss - root styles in sass
    │ │ ├── style.scss - styling for the whole product
    │ │ ├── style.css - compiled css file
  │ │ ├── js/
    │ │ ├── type.js - auto type animation
```

## Screenshots
![image](https://github.com/KevKibe/Mail-QA/assets/86055894/1b1fa4d2-4eff-4fdc-9568-0f583d1bf22b)

![image](https://github.com/KevKibe/Mail-QA/assets/86055894/34ec481e-e552-4f7b-9181-a3a837ca2358)

![image](https://github.com/KevKibe/Mail-QA/assets/86055894/9a4e6f62-a7d9-4ea2-a22d-f13d9ba55857)

![WhatsApp Image 2023-09-03 at 09 20 03](https://github.com/KevKibe/Mail-QA/assets/86055894/1e468c53-eed8-4b34-989d-201dacc64645)

![WhatsApp Image 2023-09-02 at 12 54 52](https://github.com/KevKibe/Mail-QA/assets/86055894/5c6d1c51-d726-464d-917b-d01c31760091)

## User Journey
![image](https://github.com/KevKibe/Mail-QA/assets/86055894/dc39adba-d6b2-4885-b26b-a5a16f66aaf8)

