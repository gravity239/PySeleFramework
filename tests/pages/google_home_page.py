from selenpy.element.text_box import TextBox
from selenpy.support.conditions import be, have
from selenpy.support import browser


class GoogleHomePage():
    
    _txt_search = TextBox("name=q")

    def __init__(self):
        pass
    
    def open_google(self):
        browser.open_url("https://google.com")
        browser.wait_until(have.title("Google"))

    def search(self, key_word):
        # self._txt_search.wait_for_visible()
        self._txt_search.wait_until(be.visible)
        self._txt_search.send_keys(key_word)
        self._txt_search.wait_until(have.value(key_word))
