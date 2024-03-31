import pytest
from selenium import webdriver

from pages.cabinet_page import CabinetPage
from pages.cabinet_profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.sign_up_page import SignupPage
from pages.main_page import MainPage
from utils.email_randomizer import generate_random_email
from utils.temp_mail_plus_api import TempMailAPI


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def registered_account(driver):
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

    mail_api = TempMailAPI(email)
    password = mail_api.get_password_from_email('Confirmation of registration')
    credentials = {'email': email, 'password': password}

    return credentials


@pytest.fixture
def registered_account_without_verification(driver, registered_account):
    cabinet_page = CabinetPage(driver)
    cabinet_page.click_profile_button()

    profile_page = ProfilePage(driver)
    profile_page.click_logout()

    return registered_account


@pytest.fixture
def registered_account_with_verification(driver, registered_account_without_verification):
    email = registered_account_without_verification['email']
    mail_api = TempMailAPI(email)
    verification_link = mail_api.get_confirm_link_from_email('Confirmation of registration')
    driver.get(verification_link)

    return registered_account_without_verification
