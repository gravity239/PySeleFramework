from selenpy.support.conditions import be, have
from selenpy.support import browser
from tests.pages.home_page.google_home_page_desktop import GoogleHomePageDesktop


class GoogleHomePageMobile(GoogleHomePageDesktop):

    def open_google(self):
        browser.open_url("https://bing.com")
        browser.wait_until(have.title("Bing"))

    def search(self, key_word):
        # self._txt_search.wait_for_visible()
        self._txt_search.wait_until(be.visible)
        self._txt_search.send_keys(key_word)
        self._txt_search.wait_until(have.value(key_word))
