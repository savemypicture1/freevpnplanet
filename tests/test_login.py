import allure
import pytest

from pages.cabinet_profile_page import ProfilePage
from pages.login_page import LoginPage


@allure.suite('Login page')
@allure.title('Login with no verifying account')
def test_login_with_no_verifying_account(driver, registered_account_without_verification):
    email = registered_account_without_verification['email']
    password = registered_account_without_verification['password']

    with allure.step(f'Login with no verifying account, email: {email}, password: {password}'):
        log_in_page = LoginPage(driver)
        log_in_page.open()
        log_in_page.enter_email(email)
        log_in_page.enter_password(password)

    with allure.step('Click on log in button'):
        log_in_page.click_login_button()

    profile = ProfilePage(driver)

    assert profile.get_email() == email, 'Wrong email'
    assert profile.get_account_status() == 'Inactive', 'Wrong status'
    assert profile.get_tariff_plan() == 'Free', 'Wrong tariff plan'
    assert profile.get_tariff_validity_period(), 'Wrong tariff period'
    assert profile.verify_account_button_is_visible(), 'No verify account button'
    assert profile.get_history_table_text() == 'Payment history is empty', 'Wrong history'


@allure.suite('Login page')
@allure.title('Login with verifying account')
def test_login_with_verifying_account(driver, registered_account_with_verification):
    email = registered_account_with_verification['email']
    password = registered_account_with_verification['password']

    with allure.step(f'Login with verifying account, email: {email}, password: {password}'):
        log_in_page = LoginPage(driver)
        log_in_page.open()
        log_in_page.enter_email(email)
        log_in_page.enter_password(password)

    with allure.step('Click on log in button'):
        log_in_page.click_login_button()

    profile = ProfilePage(driver)

    assert profile.get_email() == email, 'Wrong email'
    assert profile.get_account_status() == 'Active', 'Wrong status'
    assert profile.get_tariff_plan() == 'Free', 'Wrong tariff plan'
    assert profile.get_tariff_validity_period(), 'Wrong tariff period'
    assert profile.verify_account_button_is_not_visible(), 'Verify button is present'
    assert profile.get_history_table_text() == 'Payment history is empty', 'Wrong history'


@allure.suite('Login page')
@allure.title('Login with incorrect data')
@pytest.mark.parametrize('email, password', [('', ''),
                                             ('  ', '  '),
                                             ('test@test.com', 'password')])
def test_login_with_incorrect_data(driver, open_login_page, email, password):
    with allure.step(f'Enter incorrect data, email: {email}, password: {password}'):
        log_in_page = LoginPage(driver)
        log_in_page.enter_email(email)
        log_in_page.enter_password(password)

    with allure.step('Click on log in button'):
        log_in_page.click_login_button()

    error_message = log_in_page.get_error_message()

    assert error_message == 'Wrong email or password', 'Wrong error message'


@allure.suite('Login page')
@allure.title('Login registered account with incorrect password')
def test_login_registered_account_with_incorrect_password(driver, registered_account_without_verification):
    email = registered_account_without_verification['email']
    password = 'testpassword'

    with allure.step(f'Enter registered account with incorrect password, email: {email}, password: {password}'):
        log_in_page = LoginPage(driver)
        log_in_page.open()
        log_in_page.enter_email(email)
        log_in_page.enter_password(password)

    with allure.step('Click on log in button'):
        log_in_page.click_login_button()

    error_message = log_in_page.get_error_message()

    assert error_message == 'Wrong email or password', 'Wrong error message'
