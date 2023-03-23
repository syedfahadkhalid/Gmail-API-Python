from configs import Config
from gmail_auth import GmailAuth
from email_ops import Email

def main():
    Config().load_configs()
    GmailAuth().authentication(Config().scope,Config().tokenJson,Config().credentialsJson)

    message = Email().create_message(Config().recipent, Config().subject, Config().body)
    Email().send_email(message,GmailAuth().service)

    messages = Email().search_messages(Config().keywords ,GmailAuth().service)
    Email().print_messages_details(messages,GmailAuth().service)

if __name__ == "__main__":
    main()