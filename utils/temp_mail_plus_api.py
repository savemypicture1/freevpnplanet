import datetime
import requests
from utils.parse_mail import parser


class TempMailAPI:
    BASE_URL = 'https://tempmail.plus/api/mails'

    def __init__(self, email: str):
        self.email = email

    def get_mails(self) -> object:
        response = requests.get(self.BASE_URL + f'?email={self.email}')
        response_data = response.json()

        return response_data

    def get_mail_id(self) -> int:
        response_data = self.get_mails()
        mail_id = response_data['mail_list'][0]['mail_id']

        return mail_id

    def get_mail(self) -> str:
        mail_id = self.get_mail_id()
        response = requests.get(self.BASE_URL + f'/{mail_id}?email={self.email}')
        response_data = response.json()
        message = response_data['html']

        return message

    def get_password_from_email(self, subject: str) -> str | None:
        if not self.email_is_recieved(subject):
            raise Exception('Email is not recieved')

        message = self.get_mail()

        return parser.get_password(message)

    def get_confirm_link_from_email(self, subject: str) -> str | None:
        if not self.email_is_recieved(subject):
            raise Exception('Email is not recieved')

        message = self.get_mail()

        return parser.get_confirm_link(message)

    def email_is_recieved(self, subject: str) -> bool:
        end_time = datetime.datetime.now() + datetime.timedelta(seconds=20)

        while True:
            if datetime.datetime.now() >= end_time:
                return False

            mails = self.get_mails()

            if mails['count'] > 0 and \
                    mails['mail_list'][0]['from_mail'] == 'service@freevpnplanet.com' and \
                    mails['mail_list'][0]['subject'] == subject:
                return True
