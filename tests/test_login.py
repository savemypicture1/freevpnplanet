from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_login(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_log_in_button()

    log_in_page = LoginPage(driver)
    title = log_in_page.get_title()

    assert title == 'Sign in'
