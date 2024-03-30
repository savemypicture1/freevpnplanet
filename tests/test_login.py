from pages.cabinet_profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_login(driver, registered_account_without_verification):
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
    assert profile.verify_account_button(), 'No verify account button'
