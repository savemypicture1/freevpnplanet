import pytest

from pages.cabinet_profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_login_with_no_verifying_account(driver, registered_account_without_verification):
    email = registered_account_without_verification['email']
    password = registered_account_without_verification['password']
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_log_in_button()

    log_in_page = LoginPage(driver)
    log_in_page.enter_email(email)
    log_in_page.enter_password(password)
    log_in_page.click_login_button()

    profile = ProfilePage(driver)

    assert profile.get_email() == email, 'Wrong email'
    assert profile.get_account_status() == 'Inactive', 'Wrong status'
    assert profile.get_tariff_plan() == 'Free', 'Wrong tariff plan'
    assert profile.get_tariff_validity_period(), 'Wrong tariff period'
    assert profile.verify_account_button_is_visible(), 'No verify account button'
    assert profile.get_history_table_text() == 'Payment history is empty', 'Wrong history'


def test_login_with_verifying_account(driver, registered_account_with_verification):
    email = registered_account_with_verification['email']
    password = registered_account_with_verification['password']
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_log_in_button()

    log_in_page = LoginPage(driver)
    log_in_page.enter_email(email)
    log_in_page.enter_password(password)
    log_in_page.click_login_button()

    profile = ProfilePage(driver)

    assert profile.get_email() == email, 'Wrong email'
    assert profile.get_account_status() == 'Active', 'Wrong status'
    assert profile.get_tariff_plan() == 'Free', 'Wrong tariff plan'
    assert profile.get_tariff_validity_period(), 'Wrong tariff period'
    assert profile.verify_account_button_is_not_visible(), 'Verify button is present'
    assert profile.get_history_table_text() == 'Payment history is empty', 'Wrong history'


@pytest.mark.parametrize('email, password', [('', ''),
                                             ('  ', '  '),
                                             ('test@test.com', 'password')])
def test_login_with_incorrect_data(driver, email, password):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_log_in_button()

    log_in_page = LoginPage(driver)
    log_in_page.enter_email(email)
    log_in_page.enter_password(password)
    log_in_page.click_login_button()

    error_message = log_in_page.get_error_message()

    assert error_message == 'Wrong email or password', 'Wrong error message'


def test_login_registered_account_with_incorrect_password(driver, registered_account_without_verification):
    email = registered_account_without_verification['email']
    password = 'testpassword'
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_log_in_button()

    log_in_page = LoginPage(driver)
    log_in_page.enter_email(email)
    log_in_page.enter_password(password)
    log_in_page.click_login_button()

    error_message = log_in_page.get_error_message()

    assert error_message == 'Wrong email or password', 'Wrong error message'