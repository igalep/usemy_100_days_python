import pprint

from twilio.rest import Client
from sample_proj.stock_prices.api_clients.base_client import BaseClient

class TwilioIntegration(BaseClient):
    def __init__(self):
        super().__init__()
        self.twilio_trial_number = '+17794446217'
        self.account_sid = ''
        self.auth_token = ''
        
        self._get_api_key()
        self.client = Client(self.account_sid, self.auth_token)


    def _get_api_key(self):
        data = {
            'path': '/twilio',
            'version': 1,
            'mount' : 'udemy_course'
        }
        
        twilio_access = self.vault.pull_data(**data)
        self.account_sid = twilio_access['account_sid']
        self.auth_token = twilio_access['auth_token']
        self.api_secret = twilio_access['api_secret']
        self.api_sid = twilio_access['api_sid']

        # print(f'account_sid = {self.account_sid} , auth_token = {self.auth_token}')

    def send_sms(self, **kwargs):
        message = self.client.messages.create(
            body=kwargs['body'],
            from_=self.twilio_trial_number,
            to=kwargs['to']
        )

        pprint.pprint(message.body)


t = TwilioIntegration()
sms_data = {
   'body' : 'This is a test message for twilio',
    'to' : '+447537990755'
}

t.send_sms(**sms_data)