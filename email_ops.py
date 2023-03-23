from googleapiclient.errors import HttpError
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

class Email:

    def __init__(self):
        pass

    def send_email(self,message,service):
        logging.info('Sending Email')
        try:
            send_message = (service.users().messages().send(userId="me", body=message).execute())
            logging.info(f'sent Message Id: {send_message["id"]}')
        except HttpError as error:
            logging.info(f'An error occurred: {error}')
            send_message = None
        return send_message

    def create_message(self,to, subject, body):
        logging.info('Creating Email Message')
        message = MIMEMultipart()
        text = MIMEText(body)
        message.attach(text)
        message['to'] = to
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    
    def search_messages(self, keywords,service):
        logging.info('Searching Email')
        # Search of messages accross mailbox having one or more keyowrd in either subject or in the body
        query = ' OR '.join(['subject:' + k+' OR body:'+k for k in keywords])
        result = service.users().messages().list(userId="me", q=query).execute()
        messages = [ ]
        if 'messages' in result:
            messages.extend(result['messages'])

        while 'nextPageToken' in result:
            page_token = result['nextPageToken']
            result = service.users().messages().list(userId="me", q=query, pageToken=page_token).execute()
            if 'messages' in result:
                messages.extend(result['messages'])

        return messages
    
    def print_messages_details(self,messages,service):
        logging.info('Printing Email Detail')
        if messages:
            print(f'Total filtered messages: {len(messages)}')
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                if 'SENT' in msg['labelIds']:
                    self.print_sent_message(msg,message['id'])
                elif 'INBOX' in msg['labelIds']:
                    self.print_inbox_message(msg,message['id'])

    def print_sent_message(self,msg,msgId):
        print(f'===== Message ID:{msgId} =====')
        print(f'To: {msg["payload"]["headers"][3]["value"]}')
        print(f'Subject: {msg["payload"]["headers"][4]["value"]}')
        print(f'Date: {msg["payload"]["headers"][5]["value"]}')
        print('Mainbox: SENT')

    def print_inbox_message(self,msg,msgId):
        print(f'===== Message ID:{msgId} =====')
        print(f'From: {msg["payload"]["headers"][21]["value"]}')
        print(f'Subject: {msg["payload"]["headers"][23]["value"]}')
        print(f'Date: {msg["payload"]["headers"][18]["value"]}')
        print('Mainbox: INBOX')
  
