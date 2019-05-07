from selenpy.support.conditions import be, have
from selenpy.support import browser
from tests.pages.home_page.google_home_page import GoogleHomePage

class GoogleHomePageDesktop(GoogleHomePage):
    def __init__(self):
        GoogleHomePage.__init__(self)


    def open_google(self):
        browser.open_url("https://google.com")
        browser.wait_until(have.title("Google"))

    def search(self, key_word):
        # self._txt_search.wait_for_visible()
        self._txt_search.wait_until(be.visible)
        self._txt_search.send_keys(key_word)
        self._txt_search.wait_until(have.value(key_word))
