import requests
from utils.email_randomizer import generate_random_email
from utils.parse_mail import parser


class TempMailAPI:
    BASE_URL = 'https://tempmail.plus/api/mails'

    def __init__(self):
        self.email = generate_random_email()

    def get_mail_id(self) -> int:
        response = requests.get(self.BASE_URL + f'?email={self.email}')
        response_data = response.json()

        return response_data['mail_list'][0]['mail_id']

    def get_mail(self) -> str:
        mail_id = self.get_mail_id()
        response = requests.get(self.BASE_URL + f'/{mail_id}?email={self.email}')
        response_data = response.json()
        message = response_data['text']

        return message

    def get_password_from_email(self) -> str | None:
        message = self.get_mail()

        return parser.get_password(message)

    def get_confirm_link_from_email(self) -> str | None:
        message = self.get_mail()

        return parser.get_confirm_link(message)
