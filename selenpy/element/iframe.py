from selenpy.element.base_element import BaseElement


class IFrame(BaseElement):
    
    def __init__(self, locator):
        super().__init__(locator)    

    def switch_to(self): 
        self._driver.switch_to.frame(self.find_element())        
