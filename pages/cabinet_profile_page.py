from pages.cabinet_page import CabinetPage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(CabinetPage):
    PAGE_URL = Links.PROFILE_PAGE

    LOGOUT = ('css selector', '.title-exit')
    EMAIL = ('css selector', '.user-email b')
    ACCOUNT_STATUS = ('css selector', '.user-account-status__status')
    PLAN = ('css selector', '.details-row b')
    TARIFF_VALIDITY_PERIOD = ('css selector', '.details-col svg')
    VERIFY_ACCOUNT_BUTTON = ('css selector', '.sending button')

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT)).click()

    def get_email(self):
        return self.wait.until(EC.visibility_of_element_located(self.EMAIL)).text

    def get_account_status(self):
        return self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_STATUS)).text

    def get_tariff_plan(self):
        return self.wait.until(EC.visibility_of_element_located(self.PLAN)).text

    def get_tariff_validity_period(self):
        return self.wait.until(EC.visibility_of_element_located(self.TARIFF_VALIDITY_PERIOD))

    def verify_account_button(self):
        return self.wait.until(EC.visibility_of_element_located(self.VERIFY_ACCOUNT_BUTTON))

    def click_verify_account_button(self):
        self.wait.until(EC.element_to_be_clickable(self.VERIFY_ACCOUNT_BUTTON)).click()
