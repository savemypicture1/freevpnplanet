import allure
import pytest
from base.base_test import BaseTest
from utils.email_randomizer import generate_random_email
from utils.temp_mail_plus_api import TempMailAPI


@allure.feature('Registration')
class TestRegistration(BaseTest):
    @allure.title('Test registration')
    def test_registration(self, open_registration_page):
        email = generate_random_email()
        self.signup_page.enter_email(email)
        self.signup_page.click_create_button()
        self.signup_page.click_next_button()
        title = self.download_page.get_title()
        mail_api = TempMailAPI(email)

        assert title == 'Download Planet VPN for your devices', 'Wrong title'
        assert mail_api.email_is_recieved('Confirmation of registration'), 'No email'

    @allure.title('Test verification after registration')
    def test_verification_after_registration(self, driver, registered_account_without_verification):
        email = registered_account_without_verification['email']
        mail_api = TempMailAPI(email)

        with allure.step('Getting verification link'):
            verification_link = mail_api.get_confirm_link_from_email('Confirmation of registration')

        with allure.step('Open verification link'):
            driver.get(verification_link)

        assert self.profile_page.get_account_status() == 'Active', 'Wrong account status'

    @allure.title('Test registration with already registered account')
    def test_registration_with_already_registered_account(self, registered_account_without_verification):
        email = registered_account_without_verification['email']
        self.signup_page.open()
        self.signup_page.enter_email(email)
        self.signup_page.click_create_button()
        error_msg = self.signup_page.get_error_msg()

        assert error_msg == 'The email has already been taken', 'No error message'

    @allure.title('Test registration with incorrect email')
    @pytest.mark.parametrize('email',
                             ['thisisnotemail', '  ', ''])
    def test_registration_with_incorrect_email(self, open_registration_page, email):
        self.signup_page.enter_email(email)
        self.signup_page.click_create_button()
        error_msg = self.signup_page.get_error_msg()

        assert error_msg == 'Wrong email', 'No error message'
