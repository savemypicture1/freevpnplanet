from base.base_page import BasePage


class CabinetPage(BasePage):
    PROFILE = ('css selector', '[href="/cabinet/?page=profile"]')
    DOWNLOAD = ('css selector', '[href="/cabinet/download/"]')
    CONFIGURATIONS = ('css selector', '[href="/cabinet/configuration/"]')

    def get_title(self) -> str:
        return self.get_text(self.TITLE)

    def click_profile_button(self) -> None:
        self.click(self.PROFILE, 'profile')
