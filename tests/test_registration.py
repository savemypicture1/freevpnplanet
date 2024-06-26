import allure
import pytest

from pages.cabinet_profile_page import ProfilePage
from pages.sign_up_page import SignupPage
from pages.cabinet_download_page import DownloadPage
from utils.email_randomizer import generate_random_email
from utils.temp_mail_plus_api import TempMailAPI


@allure.suite('Registration page')
@allure.feature('Registration')
@allure.title('Test registration')
def test_registration(driver, open_registration_page):
    email = generate_random_email()

    with allure.step(f'Enter valid email: {email}'):
        signup_page = SignupPage(driver)
        signup_page.enter_email(email)

    with allure.step('Click on create button'):
        signup_page.click_create_button()

    with allure.step('Click on next button'):
        signup_page.click_next_button()

    download_page = DownloadPage(driver)
    title = download_page.get_title()
    mail_api = TempMailAPI(email)

    assert title == 'Download Planet VPN for your devices', 'Wrong title'
    assert mail_api.email_is_recieved('Confirmation of registration'), 'No email'


@allure.suite('Registration page')
@allure.feature('Registration')
@allure.title('Test verification after registration')
def test_verification_after_registration(driver, registered_account_without_verification):
    email = registered_account_without_verification['email']
    mail_api = TempMailAPI(email)

    with allure.step('Getting verification link'):
        verification_link = mail_api.get_confirm_link_from_email('Confirmation of registration')

    with allure.step('Open verification link'):
        driver.get(verification_link)

    profile_page = ProfilePage(driver)

    assert profile_page.get_account_status() == 'Active', 'Wrong account status'


@allure.suite('Registration page')
@allure.feature('Registration')
@allure.title('Test registration with already registered account')
def test_registration_with_already_registered_account(driver, registered_account_without_verification):
    email = registered_account_without_verification['email']

    with allure.step(f'Enter registered email: {email}'):
        signup_page = SignupPage(driver)
        signup_page.open()
        signup_page.enter_email(email)

    with allure.step('Click on create button'):
        signup_page.click_create_button()

    error_msg = signup_page.get_error_msg()

    assert error_msg == 'The email has already been taken', 'No error message'


@allure.suite('Registration page')
@allure.feature('Registration')
@allure.title('Test registration with incorrect email')
@pytest.mark.parametrize('email',
                         ['thisisnotemail', '  ', ''])
def test_registration_with_incorrect_email(driver, open_registration_page, email):
    with allure.step(f'Enter incorrect email: {email}'):
        signup_page = SignupPage(driver)
        signup_page.enter_email(email)

    with allure.step('Click on create button'):
        signup_page.click_create_button()

    error_msg = signup_page.get_error_msg()

    assert error_msg == 'Wrong email', 'No error message'
