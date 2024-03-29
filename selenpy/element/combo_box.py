from selenpy.element.base_element import BaseElement
from selenium.webdriver.support.ui import Select


class ComboBox(BaseElement):

    def __init__(self, locator, parent=None):
        super().__init__(locator, parent)
        self._s = None
    
    @property
    def _select(self):
        if self._s is None:
            self._s = Select(self.element)
        return self._s

    def select_by_value(self, value):        
        self._select.select_by_value(value)
        
    def select_by_index(self, idx):    
        self._select.select_by_index(idx)
        
    def select_by_visible_text(self, text):
        self._select.select_by_visible_text(text)
    
    @property
    def first_selected_text(self):        
        return self._select.first_selected_option.text
        
