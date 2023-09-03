# Mail-QA
Mail QA is a chat-based web application that is focused on addressing the issue of professionals spending a significant portion of their workday on email communication. 
The proposed solution involves using generative AI to streamline email management and improve productivity.<br>
This repository contains the source code and development history of the Mail QA platform.

## How we are Solving the Problem
The proposed solution involves using generative AI specifically OpenAI models to streamline email management
and improve productivity.<br>
Here's a breakdown of the key components:
- Chat-based interface to access any information in the user’s email content to perform actions such as, searching for specific email or summarizing a bunch emails.
- Support for 98 languages as currently supported by the OpenAI API ensuring that users from diverse linguistic backgrounds can translate emails in any language.
- Generate concise responses to emails based on user requests.


## Structure
```
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
| │ │ ├── index.html - signup page
│ │ ├── login/
| │ │ ├── index.html - login page
│ │ ├── prompt/
| │ │ ├── index.html - prompt page
│ │ ├── assets/
| │ │ ├── css/
| | │ │ ├── _root.scss - root styles in sass
| | │ │ ├── style.scss - styling for the whole product
| | │ │ ├── style.css - compiled css file
| │ │ ├── js/
|   │ │ ├── type.js - auto type animation

│ ├── public/
│ │ ├── index.html - configuration file
│ │ ├── logo.png - logo for the website
│ │ ├── manifest.json - configuration file
│ │ ├── 145862897_padded_logo.png - configuration file

│ ├── scripts/
│ │ ├── build.js - to build markup code
│ │ ├── start.js - starts the server on localhost
│ │ ├── test.js - for debugging server

│ ├── src/
│ │ ├── App.js -homepage
│ │ ├── App.css - styling for homepage
│ │ ├── index.js - configuration file
│ │ ├── index.css - configuration file
│ │ ├── signup/
| │ │ ├── signup.js - signup page
│ │ ├── login/
| │ │ ├── login.js - login page

│ │ ├── assets/
| │ │ ├── css/
| │ │ ├── _root.scss - root styles in sass
| | │ │ ├── style.scss - styling for the whole product
| │ │ ├── style.css - compiled css file
| │ │ ├── js/
| | │ │ ├── type.js - auto type animation
| │ │ ├── img/
| │ │ ├── envelope.png - image of envelope
| │ │ ├── logo.png - image of logo
| │ │ ├── mailcart.png - image of mailcart
| │ │ ├── messages.png - image of a messaged inbox
| │ │ ├── logo.png - logo for the website

│ │ ├── .gitignore - excludes dependancies
│ │ ├── LICENSE - UI License
│ │ ├── README.md - for debugging server
│ │ ├── index.js - config file
│ │ ├── package-lock.json - config file
│ │ ├── package.json - config file
```

## Screenshots
![image](https://github.com/KevKibe/Mail-QA/assets/86055894/1b1fa4d2-4eff-4fdc-9568-0f583d1bf22b)

![image](https://github.com/KevKibe/Mail-QA/assets/86055894/34ec481e-e552-4f7b-9181-a3a837ca2358)

![image](https://github.com/KevKibe/Mail-QA/assets/86055894/9a4e6f62-a7d9-4ea2-a22d-f13d9ba55857)

![WhatsApp Image 2023-09-03 at 09 20 03](https://github.com/KevKibe/Mail-QA/assets/86055894/1e468c53-eed8-4b34-989d-201dacc64645)
![image](https://github.com/KevKibe/Mail-QA/assets/86055894/2c3f843d-48db-4d03-8369-15ac1b712a93)
![image](https://github.com/KevKibe/Mail-QA/assets/86055894/43453072-e632-49c9-89ab-a9e3fbe0e7e2)
![image](https://github.com/KevKibe/Mail-QA/assets/86055894/0a85408f-6740-4f96-89b8-93be2bb90265)
![image](https://github.com/KevKibe/Mail-QA/assets/86055894/122c7a67-72b0-4269-ab18-480041751c8a)
![image](https://github.com/KevKibe/Mail-QA/assets/86055894/cee5ac9d-480e-4e27-b3ee-18100a0916aa)






![WhatsApp Image 2023-09-02 at 12 54 52](https://github.com/KevKibe/Mail-QA/assets/86055894/5c6d1c51-d726-464d-917b-d01c31760091)

## User Journey
![image](https://github.com/KevKibe/Mail-QA/assets/86055894/dc39adba-d6b2-4885-b26b-a5a16f66aaf8)

