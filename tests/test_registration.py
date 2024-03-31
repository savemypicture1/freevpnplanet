import pytest

from pages.cabinet_profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.sign_up_page import SignupPage
from pages.cabinet_download_page import DownloadPage
from pages.main_page import MainPage
from utils.email_randomizer import generate_random_email
from utils.temp_mail_plus_api import TempMailAPI


def test_registration(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_log_in_button()

    login_page = LoginPage(driver)
    login_page.click_sign_up()

    signup_page = SignupPage(driver)
    email = generate_random_email()
    signup_page.enter_email(email)
    signup_page.click_create_button()
    signup_page.click_next_button()

    download_page = DownloadPage(driver)
    title = download_page.get_title()
    mail_api = TempMailAPI(email)

    assert title == 'Download Planet VPN for your devices', 'Wrong title'
    assert mail_api.email_is_recieved('Confirmation of registration'), 'No email'


def test_verification_after_registration(driver, registered_account_without_verification):
    email = registered_account_without_verification['email']
    mail_api = TempMailAPI(email)
    verification_link = mail_api.get_confirm_link_from_email('Confirmation of registration')
    driver.get(verification_link)

    profile_page = ProfilePage(driver)

    assert profile_page.get_account_status() == 'Active', 'Wrong account status'


def test_registration_with_already_registered_account(driver, registered_account_without_verification):
    email = registered_account_without_verification['email']
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_log_in_button()

    login_page = LoginPage(driver)
    login_page.click_sign_up()

    signup_page = SignupPage(driver)
    signup_page.enter_email(email)
    signup_page.click_create_button()

    error_msg = signup_page.get_error_msg()

    assert error_msg == 'The email has already been taken', 'No error message'


@pytest.mark.parametrize('email',
                         ['thisisnotemail', '  ', ''])
def test_registration_with_incorrect_email(driver, email):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_log_in_button()

    login_page = LoginPage(driver)
    login_page.click_sign_up()

    signup_page = SignupPage(driver)
    signup_page.enter_email(email)
    signup_page.click_create_button()

    error_msg = signup_page.get_error_msg()

    assert error_msg == 'Wrong email', 'No error message'
