import os

from playwright.sync_api import Page, expect


class WebDriver:
    page = None
    url = os.getenv("BASE_URL")

    @classmethod
    def __init__(cls, page: Page):
        cls.page = page

    def go_to_page(self):
        """
        Go to page
        """
        self.page.wait_for_load_state()
        self.page.goto(self.url)

    def fill_field(self, locator: str, value: str):
        self.page.wait_for_load_state()
        self.page.fill(locator, value)

    def click(self, locator: str):
        self.page.wait_for_load_state()
        self.page.click(locator)

    def am_on_page(self, url: str):
        """
        Check I am on selected page
        Args:
            url: str: full url address of page
        """
        self.page.wait_for_load_state()
        expect(self.page).to_have_url(url)

    def url_contains(self, path: str):
        """
        Check path is present in current url
        Args:
            path: str: path to be search in url
        """
        self.page.wait_for_load_state()
        assert path in self.page.url

    def see_text(self, text: str, locator: str = None):
        """
        Check is text present on page
        Args:
            text: text to be found
            locator: optional: place where to search
        """
        if locator is None:
            locator = "//*"
        self.page.wait_for_load_state()
        expect(self.page.locator(locator)).to_have_text(text)

    def dont_see_text(self, text: str, locator: str = None):
        """
        Check is text not present on page
        Args:
            text: text to be not found
            locator: optional: place where to search
        """
        if locator is None:
            locator = "//*"
        self.page.wait_for_load_state()
        expect(self.page.locator(locator)).to_have_text(text)

    def see_element(self, locator: str):
        """
        Check is element present on page
        Args:
            locator: place where to search
        """
        self.page.wait_for_load_state()
        expect(self.page.locator(locator)).to_be_visible()

    def dont_see_element(self, locator: str):
        """
        Check is element not present on page
        Args:
            locator: place where to search
        """
        self.page.wait_for_load_state()
        expect(self.page.locator(locator)).not_to_be_visible()
