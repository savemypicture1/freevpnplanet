import allure
import pytest
from base.base_test import BaseTest


@allure.feature('Login')
class TestLogin(BaseTest):
    @allure.title('Login with no verifying account')
    def test_login_with_no_verifying_account(self, registered_account_without_verification):
        email = registered_account_without_verification['email']
        password = registered_account_without_verification['password']
        self.login_page.open()
        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()

        assert self.profile_page.get_email() == email, 'Wrong email'
        assert self.profile_page.get_account_status() == 'Inactive', 'Wrong status'
        assert self.profile_page.get_tariff_plan() == 'Free', 'Wrong tariff plan'
        assert self.profile_page.get_tariff_validity_period(), 'Wrong tariff period'
        assert self.profile_page.verify_account_button_is_visible(), 'No verify account button'
        assert self.profile_page.get_history_table_text() == 'Payment history is empty', 'Wrong history'

    @allure.title('Login with verifying account')
    def test_login_with_verifying_account(self, registered_account_with_verification):
        email = registered_account_with_verification['email']
        password = registered_account_with_verification['password']
        self.login_page.open()
        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()

        assert self.profile_page.get_email() == email, 'Wrong email'
        assert self.profile_page.get_account_status() == 'Active', 'Wrong status'
        assert self.profile_page.get_tariff_plan() == 'Free', 'Wrong tariff plan'
        assert self.profile_page.get_tariff_validity_period(), 'Wrong tariff period'
        assert self.profile_page.verify_account_button_is_not_visible(), 'Verify button is present'
        assert self.profile_page.get_history_table_text() == 'Payment history is empty', 'Wrong history'

    @allure.title('Login with incorrect data')
    @pytest.mark.parametrize('email, password', [('', ''),
                                                 ('  ', '  '),
                                                 ('test@test.com', 'password')])
    def test_login_with_incorrect_data(self, open_login_page, email, password):
        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
        error_message = self.login_page.get_error_message()

        assert error_message == 'Wrong email or password', 'Wrong error message'

    @allure.title('Login registered account with incorrect password')
    def test_login_registered_account_with_incorrect_password(self, registered_account_without_verification):
        email = registered_account_without_verification['email']
        password = 'testpassword'
        self.login_page.open()
        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
        error_message = self.login_page.get_error_message()

        assert error_message == 'Wrong email or password', 'Wrong error message'
