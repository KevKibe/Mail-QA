<<<<<<< HEAD
# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
=======
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

## Resources
[Demo Video](https://drive.google.com/file/d/1ivAI7riE9yAOSYZ1-nWHpN8l8szX46EW/view?usp=sharing) <br>
[Pitch Deck](https://docs.google.com/presentation/d/12jkcWXsaLJO9XR5Z7PLDtkm17liagl22xOLddlPp6fQ/edit?usp=sharing)

## Screenshots
![image](https://github.com/KevKibe/Mail-QA/assets/86055894/1b1fa4d2-4eff-4fdc-9568-0f583d1bf22b)

![image](https://github.com/KevKibe/Mail-QA/assets/86055894/34ec481e-e552-4f7b-9181-a3a837ca2358)

![image](https://github.com/KevKibe/Mail-QA/assets/86055894/9a4e6f62-a7d9-4ea2-a22d-f13d9ba55857)

![image](https://github.com/KevKibe/Mail-QA/assets/86055894/e1f9c62e-9de6-4c5b-989d-5581ed0e5537)


![image](https://github.com/KevKibe/Mail-QA/assets/86055894/43453072-e632-49c9-89ab-a9e3fbe0e7e2)

![image](https://github.com/KevKibe/Mail-QA/assets/86055894/0a85408f-6740-4f96-89b8-93be2bb90265)

![image](https://github.com/KevKibe/Mail-QA/assets/86055894/122c7a67-72b0-4269-ab18-480041751c8a)

![image](https://github.com/KevKibe/Mail-QA/assets/86055894/cee5ac9d-480e-4e27-b3ee-18100a0916aa)


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
## User Journey
![image](https://github.com/KevKibe/Mail-QA/assets/86055894/dc39adba-d6b2-4885-b26b-a5a16f66aaf8)

>>>>>>> 72c98daff0058448ced58be53d7357940333543c
