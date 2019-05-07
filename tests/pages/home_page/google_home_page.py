from selenpy.element.text_box import TextBox
from tests.pages.page_base import PageBase


class GoogleHomePage(PageBase):
    def __init__(self):
        PageBase.__init__(self, "GoogleHomePage")
        # self.initial_elements()

    def init_elements(self):
        self._txt_search = TextBox(self.create_locator("_txt_search_locator"))

    # _txt_search = TextBox("name=q")

    def open_google(self):
        pass

    def search(self, key_word):
       pass
