from env_variables import SCOPE,KEYWORDS,RECIPENT,SUBJECT,BODY,CREDENTIALJSON,TOKENJSON
import yaml
import logging

class Config:

    def load_configs(self):
        self.set_logging_config()
        logging.info("Fetching Configurations")

        Config.scope = list(yaml.load(open(SCOPE), Loader=yaml.FullLoader).split(' '))
        Config.keywords = list(yaml.load(open(KEYWORDS), Loader=yaml.FullLoader).split(' '))
        Config.recipent = RECIPENT
        Config.subject = SUBJECT
        Config.body = BODY
        Config.credentialsJson = CREDENTIALJSON
        Config.tokenJson = TOKENJSON

    @staticmethod
    def set_logging_config():
        logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.DEBUG,
            datefmt='%Y-%m-%d %H:%M:%S'
        )