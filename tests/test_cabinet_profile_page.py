import allure

from pages.cabinet_page import CabinetPage
from pages.cabinet_profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.temp_mail_plus_api import TempMailAPI


@allure.suite('Profile page')
@allure.feature('Profile')
@allure.title('Test change password')
def test_change_password(driver, registered_account):
    email = registered_account['email']
    password = registered_account['password']
    new_password = password + '1'

    with allure.step('Click on profile button'):
        cabinet_page = CabinetPage(driver)
        cabinet_page.click_profile_button()

    with allure.step('Click on change password button'):
        profile_page = ProfilePage(driver)
        profile_page.click_change_password_button()

    with allure.step(f'Enter old password: {password}, new passwords: {new_password}, {new_password}'):
        profile_page.enter_change_passwords(password, new_password, new_password)

    with allure.step('Click on change password button to save'):
        profile_page.click_confirm_change_password_button()

    assert profile_page.get_password_was_changed_message() == 'Password was changed', 'No password was changed message'

    with allure.step('Click logout'):
        profile_page.click_logout()

    with allure.step(f'Log in with email: {email} and password: {new_password}'):
        main_page = MainPage(driver)
        main_page.click_log_in_button()
        log_in_page = LoginPage(driver)
        log_in_page.enter_email(email)
        log_in_page.enter_password(new_password)
        log_in_page.click_login_button()

    assert profile_page.get_email() == email, 'Wrong email'
    assert profile_page.get_account_status() == 'Inactive', 'Wrong status'
    assert profile_page.get_tariff_plan() == 'Free', 'Wrong tariff plan'
    assert profile_page.get_tariff_validity_period(), 'Wrong tariff period'
    assert profile_page.get_history_table_text() == 'Payment history is empty', 'Wrong history'


@allure.suite('Profile page')
@allure.feature('Profile')
@allure.title('Test change password with incorrect old password')
def test_change_password_with_incorrect_old_password(driver, registered_account):
    with allure.step('Click on profile button'):
        cabinet_page = CabinetPage(driver)
        cabinet_page.click_profile_button()

    with allure.step('Click on change password button'):
        profile_page = ProfilePage(driver)
        profile_page.click_change_password_button()

    with allure.step('Enter incorrect old password: "password" and correct new passwords: "newpassword1"'):
        profile_page.enter_change_passwords('password', 'newpassword1', 'newpassword1')

    with allure.step('Click on change password button to save'):
        profile_page.click_confirm_change_password_button()

    assert profile_page.get_wrong_old_password_message() == 'Wrong old password', 'No error message'


@allure.suite('Profile page')
@allure.feature('Profile')
@allure.title('Test change password with different new passwords')
def test_change_password_with_different_new_passwords(driver, registered_account):
    password = registered_account['password']

    with allure.step('Click on profile button'):
        cabinet_page = CabinetPage(driver)
        cabinet_page.click_profile_button()

    with allure.step('Click on change password button'):
        profile_page = ProfilePage(driver)
        profile_page.click_change_password_button()

    with allure.step(f'Enter correct old password: {password} and different new passwords: "newpassword1" and "newpassword123"'):
        profile_page.enter_change_passwords(password, 'newpassword1', 'newpassword123')

    with allure.step('Click on change password button to save'):
        profile_page.click_confirm_change_password_button()

    assert profile_page.get_wrong_old_password_message() == 'Passwords do not match', 'No error message'


@allure.suite('Profile page')
@allure.feature('Profile')
@allure.title('Test verify account')
def test_verify_account(driver, registered_account):
    email = registered_account['email']

    with allure.step('Click on profile button'):
        cabinet_page = CabinetPage(driver)
        cabinet_page.click_profile_button()

    with allure.step('Click on verify button'):
        profile_page = ProfilePage(driver)
        profile_page.click_verify_account_button()

    with allure.step(f'Getting verification link from email {email}'):
        mail_api = TempMailAPI(email)
        verification_link = mail_api.get_confirm_link_from_email('Account Verification')

    with allure.step('Open verification link'):
        driver.get(verification_link)

    assert profile_page.get_account_status() == 'Active', 'Wrong account status'
