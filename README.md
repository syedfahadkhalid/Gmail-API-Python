# haensel-ams Recruitment Challenge

## About this porject
This project is a Python implementation of the Google Gmail API, designed to showcase the use of the API for basic email sending and searching functionality. The code is divided into two main parts: one for sending emails and one for searching for messages in the Gmail mailbox.

To use the code, you need to set up a test Gmail account and enable the Gmail API. Once you have obtained the necessary credentials, you can use the send_email function to send emails and the search_messages function to search for messages that contain specific keywords in the subject or body.

Overall, this project is a simple but effective demonstration of how to use the Google Gmail API in Python to send and search for emails, and can serve as a starting point for more complex Gmail API integrations.

## Technical Aspects
This project uses the following stack:
- Python3
- Google API

## Setup Guide
- ### Enable the Gmail API and Create Credentials
  To use the Gmail API, you need to enable it in the Google Cloud Console. Follow these steps below or you can follow <a 
  href="https://developers.google.com/gmail/api/quickstart/python">Quick Start Gude for Python</a>
  
  - Go to the <a href="https://console.developers.google.com/">Google Cloud Console.</a>
  - Click the project drop-down and select or create a project.
  - Click Continue.
  - Click the Navigation menu and select APIs & Services > Dashboard.
  - Click ENABLE APIS AND SERVICES.
  - Search for "Gmail API" and select it.
  - Click ENABLE.
  - Click Create credentials.
  - Select OAuth client ID.
  - Choose Desktop App, and give it a name.
  - Click Create.
  - Click Download to download the credentials in JSON format.
  - Rename the downloaded file to credentials.json and save it in your project directory.
- ### Install Required Packages
  To use the Google API you will need to intsall the required packages 
  ```python
  pip3 install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
  ```
- ### Run The Code
  - Clone or download the code from the repository.
  - Place the "credentials.json" file in the directory
  - Modify the Recipent Email under env_varibales.py
  - Modify the Subject & Body of the email
  - Navigate to the project directory in your terminal.
  ```python
  python main.py
  ```
  - During execution it will promt for the Google API authorzation
  - The first time you run the sample, it prompts you to authorize access:
    - If you're not already signed in to your Google Account, you're prompted to sign in. If you're signed in to multiple accounts, select one account to use for authorization.
    - Click Accept.