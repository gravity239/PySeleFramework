from selenpy.element.text_box import TextBox
from selenpy.support import browser
from selenpy.element.base_element import BaseElement


class GoogleHomePage():

    def __init__(self):
        self._txt_search = TextBox("name=q")
        self._search_form = BaseElement("id=searchform")
        self._txt_search_parent = TextBox("name=q", self._search_form)
    
    def open_google(self):
        browser.open_url("https://google.com")
        browser.wait_for_title_contains("Google")

    def search(self, key_word):
        self._txt_search.wait_for_visible()        
        self._txt_search.send_keys(key_word)
        
    def search_parent(self, key_word): 
        self._txt_search_parent.wait_for_visible()
        self._txt_search_parent.send_keys(key_word)
    
    def get_searched_value(self):
        return self._txt_search.value
        
