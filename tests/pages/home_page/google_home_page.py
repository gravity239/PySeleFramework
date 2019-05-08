from selenpy.element.text_box import TextBox
from tests.pages.page_base import PageBase
from selenpy.element.base_element import BaseElement


class GoogleHomePage(PageBase):
    def __init__(self):
        PageBase.__init__(self, "GoogleHomePage")
        self._txt_search = TextBox(self.create_locator("_txt_search_locator"))
        self._search_form = BaseElement("id=searchform")
        self._txt_search_parent = TextBox("name=q", self._search_form)
