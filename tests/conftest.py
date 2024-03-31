import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cabinet_page import CabinetPage
from pages.cabinet_profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.sign_up_page import SignupPage
from pages.main_page import MainPage
from utils.email_randomizer import generate_random_email
from utils.temp_mail_plus_api import TempMailAPI


 # Launch tests without opening browser
@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()


@pytest.fixture
def open_login_page(driver):
    with allure.step('Open the web site https://freevpnplanet.com/'):
        main_page = MainPage(driver)
        main_page.open()

    with allure.step('Click on log in button'):
        main_page.click_log_in_button()


@pytest.fixture
def open_registration_page(driver, open_login_page):
    with allure.step('Click on sign in button'):
        login_page = LoginPage(driver)
        login_page.click_sign_up()


@pytest.fixture
def registered_account(driver, open_registration_page):
    email = generate_random_email()

    with allure.step(f'Enter email: {email}'):
        signup_page = SignupPage(driver)
        signup_page.enter_email(email)

    with allure.step('Click on create button'):
        signup_page.click_create_button()

    with allure.step('Click on next button'):
        signup_page.click_next_button()

    with allure.step(f'Getting password from email: {email}'):
        mail_api = TempMailAPI(email)
        password = mail_api.get_password_from_email('Confirmation of registration')

    credentials = {'email': email, 'password': password}

    return credentials


@pytest.fixture
def registered_account_without_verification(driver, registered_account):
    with allure.step('Click on profile button'):
        cabinet_page = CabinetPage(driver)
        cabinet_page.click_profile_button()

    with allure.step('Click on logout button'):
        profile_page = ProfilePage(driver)
        profile_page.click_logout()

    return registered_account


@pytest.fixture
def registered_account_with_verification(driver, registered_account_without_verification):
    email = registered_account_without_verification['email']

    with allure.step(f'Getting link from email: {email}'):
        mail_api = TempMailAPI(email)
        verification_link = mail_api.get_confirm_link_from_email('Confirmation of registration')

    with allure.step('Open verification link'):
        driver.get(verification_link)

    return registered_account_without_verification
