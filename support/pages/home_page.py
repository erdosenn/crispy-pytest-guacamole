"""
Home page.
"""
from playwright.sync_api import Page

from support.modules.web_driver import WebDriver


class HomePage(WebDriver):
    """
    Login Page class.
    """

    """path static"""
    path = ""

    """names"""
    facebook = "facebook"
    twitter = "twitter"
    youtube = "youtube"
    google_plus = "google-plus"

    """locators"""
    _btn_login = "//*[@class='login']"

    """methods"""

    def __init__(self, page: Page):
        super().__init__(page, self.path)

    @staticmethod
    def _btn_media_locator(social_media_name: str) -> str:
        return f"//*[@id='social_block']//*[@class='{social_media_name}']"

    def go_to_login(self):
        self.click(self._btn_login)

    def go_to_facebook(self):
        with self.page.context.expect_page() as new_window:
            self.click(self._btn_media_locator(self.facebook))
        return new_window.value

    def go_to_twitter(self):
        with self.page.context.expect_page() as new_window:
            self.click(self._btn_media_locator(self.twitter))
        return new_window.value

    def go_to_youtube(self):
        with self.page.context.expect_page() as new_window:
            self.click(self._btn_media_locator(self.youtube))
        return new_window.value

    def go_to_google_plus(self):
        with self.page.context.expect_page() as new_window:
            self.click(self._btn_media_locator(self.google_plus))
        return new_window.value
