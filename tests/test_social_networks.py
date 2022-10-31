import re

import pytest
from playwright.sync_api import Page, expect

from support.modules.web_driver import WebDriver
from support.pages.home_page import HomePage


class TestSocialNetworks:
    _facebook_url = "https://www.facebook.com/groups/525066904174158/"
    _twitter_url = "https://twitter.com/seleniumfrmwrk"
    _youtube_url = "https://www.youtube.com/channel/UCHl59sI3SRjQ-qPcTrgt0tA"
    _google_plus_url = "https://accounts.google.com/signin"

    @pytest.fixture(scope="function", autouse=True)
    def go_to_home_page_and_close_tabs(self, page: Page):
        self.page = page
        self.page.goto(HomePage.url)
        if WebDriver(self.page).see_text("Reached"):
            self.page.reload()
            self.page.wait_for_timeout(3000)
        yield self.page
        pages = page.context.pages
        for page in pages[1::1]:
            page.close()

    def test_facebook(self) -> None:
        page_facebook = HomePage(self.page).go_to_facebook()
        expect(page_facebook).to_have_url(self._facebook_url)

    def test_twitter(self) -> None:
        page_twitter = HomePage(self.page).go_to_twitter()
        expect(page_twitter).to_have_url(self._twitter_url)

    def test_youtube(self) -> None:
        page_youtube = HomePage(self.page).go_to_youtube()
        page_youtube.click('//*[@aria-label="Zaakceptuj wszystko"]')
        expect(page_youtube).to_have_url(self._youtube_url)

    def test_google_plus(self) -> None:
        page_google_plus = HomePage(self.page).go_to_google_plus()
        expect(page_google_plus).to_have_url(re.compile(f"{self._google_plus_url}"))

