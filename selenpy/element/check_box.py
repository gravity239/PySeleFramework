from selenpy.element.base_element import BaseElement
from selenpy.helper.wait import wait_until


class CheckBox(BaseElement):
    
    def __init__(self, locator, parent=None):
        super().__init__(locator, parent)

    def is_checked(self):
        return self.find_element().is_selected()
    
    def check(self):
        if self.is_checked() == False: self.click()
        
    def un_check(self):
        if self.is_checked() == True: self.click()
        
    def wait_for_checked(self, timeout=None):
        wait_until(lambda: self.is_checked(),
            "Element '%s' was not checked in <TIMEOUT>." % self._locator,
            timeout)
    
    def wait_for_unchecked(self, timeout=None):
        wait_until(lambda: not self.is_checked(),
            "Element '%s' was not un-checked in <TIMEOUT>." % self._locator,
            timeout)
            
