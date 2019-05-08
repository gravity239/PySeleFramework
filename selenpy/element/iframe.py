from selenpy.element.base_element import BaseElement


class IFrame(BaseElement):
    
    def __init__(self, locator, parent=None):
        super().__init__(locator, parent) 

    def switch_to(self): 
        self._driver.switch_to.frame(self.element)        
