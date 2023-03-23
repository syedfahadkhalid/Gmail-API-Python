import os.path
import logging

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build

class GmailAuth:
   
   def __init__(self):
        pass
   
   def authentication(self,SCOPES,tokenJson,credentialsJson):
        logging.info(f'Authenticating')
        GmailAuth.creds = None
        GmailAuth.service = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        try:
            if os.path.exists(tokenJson):
                logging.info(f'{tokenJson} found')
                GmailAuth.creds = Credentials.from_authorized_user_file(tokenJson, SCOPES)
                GmailAuth.service = build('gmail', 'v1', credentials=GmailAuth.creds)
            # If there are no (valid) credentials available, let the user log in.
            if not GmailAuth.creds or not GmailAuth.creds.valid:
                if GmailAuth.creds and GmailAuth.creds.expired and GmailAuth.creds.refresh_token:
                    GmailAuth.creds.refresh(Request())
                    GmailAuth.service = build('gmail', 'v1', credentials=GmailAuth.creds)
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        credentialsJson, SCOPES)
                    GmailAuth.creds = flow.run_local_server(port=0)
                    GmailAuth.service = build('gmail', 'v1', credentials=GmailAuth.creds)
                # Save the credentials for the next run
                with open(tokenJson, 'w') as token:
                    token.write(GmailAuth.creds.to_json())
        except Exception as e:
                logging.info(f"An Error Occured: {e}")
        
        

        