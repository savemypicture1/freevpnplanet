import pytest
from pages.login_page import LoginPage
from pages.cabinet_download_page import DownloadPage
from pages.cabinet_page import CabinetPage
from pages.cabinet_profile_page import ProfilePage
from pages.main_page import MainPage
from pages.sign_up_page import SignupPage


class BaseTest:
    login_page: LoginPage
    download_page: DownloadPage
    cabinet_page: CabinetPage
    profile_page: ProfilePage
    main_page: MainPage
    signup_page: SignupPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver

        request.cls.login_page = LoginPage(driver)
        request.cls.download_page = DownloadPage(driver)
        request.cls.cabinet_page = CabinetPage(driver)
        request.cls.profile_page = ProfilePage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.signup_page = SignupPage(driver)
