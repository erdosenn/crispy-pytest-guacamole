import re

import pytest
from playwright.sync_api import Page, expect

from support.pages.home_page import HomePage


class TestSocialNetworks:
    _facebook_url = "https://www.facebook.com/groups/525066904174158/"
    _twitter_url = "https://twitter.com/seleniumfrmwrk"
    _youtube_url = "https://www.youtube.com/channel/UCHl59sI3SRjQ-qPcTrgt0tA"
    _google_plus_url = "https://accounts.google.com/signin"

    @pytest.fixture(scope="function", autouse=True)
    def go_to_page(self, page: Page):
        page.goto(HomePage.url)
        yield
        pages = page.context.pages
        for page in pages[1::1]:
            page.close()

    def test_facebook(self, page: Page) -> None:
        page_facebook = HomePage(page).go_to_facebook()
        expect(page_facebook).to_have_url(self._facebook_url)

    def test_twitter(self, page: Page) -> None:
        page_twitter = HomePage(page).go_to_twitter()
        expect(page_twitter).to_have_url(self._twitter_url)

    def test_youtube(self, page: Page) -> None:
        page_youtube = HomePage(page).go_to_youtube()
        expect(page_youtube).to_have_url(self._youtube_url)

    def test_google_plus(self, page: Page) -> None:
        page_google_plus = HomePage(page).go_to_google_plus()
        expect(page_google_plus).to_have_url(re.compile(f"{self._google_plus_url}"))
