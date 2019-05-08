from selenpy.element.base_element import BaseElement


class IFrame(BaseElement):
    
    def __init__(self, locator, parent=None):
        super().__init__(locator, parent) 

    def select(self):
        self._driver.switch_to.frame(self.element)     
        
    def unselect(self):   
        self._driver.switch_to.default_content()
