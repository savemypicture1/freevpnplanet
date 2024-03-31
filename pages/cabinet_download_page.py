from pages.cabinet_page import CabinetPage
from config.links import Links


class DownloadPage(CabinetPage):
    PAGE_URL = Links.DOWNLOAD_PAGE

    TITLE = ('css selector', '.downloads-main h2')
