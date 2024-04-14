import allure
from base.base_test import BaseTest
from utils.temp_mail_plus_api import TempMailAPI


@allure.feature('Profile')
class TestProfilePage(BaseTest):
    @allure.title('Test change password')
    def test_change_password(self, registered_account):
        email = registered_account['email']
        password = registered_account['password']
        new_password = password + '1'
        self.cabinet_page.click_profile_button()
        self.profile_page.click_change_password_button()
        self.profile_page.enter_change_passwords(password, new_password, new_password)
        self.profile_page.click_confirm_change_password_button()

        assert self.profile_page.get_password_was_changed_message() == 'Password was changed', 'No password was changed message'

        self.profile_page.click_logout()
        self.main_page.click_log_in_button()
        self.login_page.enter_email(email)
        self.login_page.enter_password(new_password)
        self.login_page.click_login_button()

        assert self.profile_page.get_email() == email, 'Wrong email'
        assert self.profile_page.get_account_status() == 'Inactive', 'Wrong status'
        assert self.profile_page.get_tariff_plan() == 'Free', 'Wrong tariff plan'
        assert self.profile_page.get_tariff_validity_period(), 'Wrong tariff period'
        assert self.profile_page.get_history_table_text() == 'Payment history is empty', 'Wrong history'

    @allure.title('Test change password with incorrect old password')
    def test_change_password_with_incorrect_old_password(self, registered_account):
        self.cabinet_page.click_profile_button()
        self.profile_page.click_change_password_button()
        self.profile_page.enter_change_passwords('password', 'newpassword1', 'newpassword1')
        self.profile_page.click_confirm_change_password_button()

        assert self.profile_page.get_wrong_old_password_message() == 'Wrong old password', 'No error message'

    @allure.title('Test change password with different new passwords')
    def test_change_password_with_different_new_passwords(self, registered_account):
        password = registered_account['password']
        self.cabinet_page.click_profile_button()
        self.profile_page.click_change_password_button()
        self.profile_page.enter_change_passwords(password, 'newpassword1', 'newpassword123')
        self.profile_page.click_confirm_change_password_button()

        assert self.profile_page.get_wrong_old_password_message() == 'Passwords do not match', 'No error message'

    @allure.title('Test verify account')
    def test_verify_account(self, driver, registered_account):
        email = registered_account['email']
        self.cabinet_page.click_profile_button()
        self.profile_page.click_verify_account_button()

        assert self.profile_page.get_send_email_pop_up() == 'An email has been sent to you to verify your account.', 'No send email pop up'

        with allure.step(f'Getting verification link from email {email}'):
            mail_api = TempMailAPI(email)
            verification_link = mail_api.get_confirm_link_from_email('Account Verification')

        with allure.step('Open verification link'):
            driver.get(verification_link)

        assert self.profile_page.get_account_status() == 'Active', 'Wrong account status'
