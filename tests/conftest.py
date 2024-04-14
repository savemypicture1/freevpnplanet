from datetime import datetime
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.email_randomizer import generate_random_email
from utils.temp_mail_plus_api import TempMailAPI


 # Launch tests without opening browser
@pytest.fixture
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sendbox")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()


# @pytest.fixture
# def driver(request):
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield driver
#     attach = driver.get_screenshot_as_png()
#     allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
#     driver.quit()


@pytest.fixture
def open_login_page(request):
    request.cls.main_page.open()
    request.cls.main_page.click_log_in_button()


@pytest.fixture
def open_registration_page(request, open_login_page):
    request.cls.login_page.click_sign_up()


@pytest.fixture
def registered_account(request, open_registration_page):
    email = generate_random_email()
    request.cls.signup_page.enter_email(email)
    request.cls.signup_page.click_create_button()
    request.cls.signup_page.click_next_button()

    with allure.step(f'Getting password from email: {email}'):
        mail_api = TempMailAPI(email)
        password = mail_api.get_password_from_email('Confirmation of registration')

    credentials = {'email': email, 'password': password}

    return credentials


@pytest.fixture
def registered_account_without_verification(request, registered_account):
    request.cls.cabinet_page.click_profile_button()
    request.cls.profile_page.click_logout()

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
