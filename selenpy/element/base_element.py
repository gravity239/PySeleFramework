from selenpy.support import browser
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenpy.helper.wait import wait_until


class BaseElement():
    
    def __init__(self, locator, parent=None):
        self._strategies = {
            'id': self.__find_by_id,
            'name': self.__find_by_name,
            'xpath': self.__find_by_xpath,
            'css': self.__find_by_css_selector,
            'class': self.__find_by_class_name
        }
        self._locator = locator
        self._dymanic_locator = locator
        self._element = None
        self._parent = parent
    
    def format(self, *args):
        self._locator = self._dymanic_locator % (args)
        self._element = None

    @property
    def element(self):
        if self._element is None:
            self.find_element()
        else:
            try:                
                self._element.is_enabled()
            except StaleElementReferenceException:
                self._element = self.find_element()                
        return self._element
    
    @property
    def text(self):
        return self.element.text
    
    @property
    def tag_name(self):
        return self.element.tag_name
    
    def get_attribute(self, name):
        return self.element.get_attribute(name)
    
    def find_elements(self):
        return self.__find(False)
    
    def find_element(self):
        return self.__find()
    
    def click(self):        
        self.wait_for_enabled()
        self.element.click()
        
    def send_keys(self, *value, append=False):      
        if not append:
            self.clear()  
        self.element.send_keys(value)
        
    def clear(self):
        self.element.clear()
        
    def is_displayed(self):
        if self.element is None:
            return False
        return self.element.is_displayed()
    
    def is_enabled(self):
        return self.element.is_enabled()
    
    def is_selected(self):
        return self.element.is_selected()
   
    def wait_for_visible(self, timeout=None):
        """Wait until element is visible
        """
        wait_until(lambda: self.is_displayed(),
            "Element '%s' not visible after <TIMEOUT>." % self._locator,
            timeout)
        
    def wait_for_invisible(self, timeout=None):
        """ Wait until element is not visible
        """
        wait_until(lambda: not self.is_displayed(),
            "Element '%s' still visible after <TIMEOUT>." % self._locator,
            timeout)
    
    def wait_for_enabled(self, timeout=None):
        """
        Waits until element is enabled.
        """
        wait_until(lambda: self.is_enabled(),
            "Element '%s' was not enabled in <TIMEOUT>." % self._locator,
            timeout)
    
    def wait_for_disabled(self, timeout=None):
        """
        Waits until element is disabled.
        """
        wait_until(lambda: not self.is_enabled(),
            "Element '%s' was not disabled in <TIMEOUT>." % self._locator,
            timeout)    
        
    def wait_for_appear(self, timeout=None):
        """Wait until element appears in DOM.
        """
        wait_until(lambda: self._find() is not None,
            "Element '%s' did not exit in <TIMEOUT>." % self._locator,
            timeout)
    
    def wait_for_disappear(self, timeout=None):
        """Wait until element disappears in DOM.
        """
        wait_until(lambda: self._find() is None,
            "Element '%s' did not exit in <TIMEOUT>." % self._locator,
            timeout)

    def wait_for_text_contains(self, text, timeout=None):
        """Wait until element contains text.
        """
        wait_until(lambda: text in self.text,
            "Element '%s' did not get text '%s' in <TIMEOUT>." % (self._locator, text),
            timeout)
    
    def wait_for_text_not_contains(self, text, timeout=None):
        """Wait until element does not contain text.
        """
        wait_until(lambda: text not in self.text,
            "Element '%s' still had text '%s' after <TIMEOUT>." % (self._locator, text),
            timeout)        
    
    # private methods
    @property
    def __driver(self):
        return browser.get_driver()
    
    def __parse_locator(self, locator):
        if locator.startswith(('//', '(//')):
            return 'xpath', locator
        index = self.__get_locator_separator_index(locator)
        if index != -1:
            prefix = locator[:index].strip()
            if prefix in self._strategies:
                return prefix, locator[index + 1:].lstrip()
        return 'default', locator
    
    def __by(self, prefix):
        if prefix == "class": 
            return By.CLASS_NAME 
        elif prefix == "css" : 
            return By.CSS_SELECTOR 
        else:
            return prefix
    
    def __get_locator_separator_index(self, locator):
        if '=' not in locator:
            return locator.find(':')
        if ':' not in locator:
            return locator.find('=')
        return min(locator.find('='), locator.find(':'))
    
    def __find(self, first_only=True):
        prefix, criteria = self.__parse_locator(self._locator)
        strategy = self._strategies[prefix]
        parent = None
        if self._parent:
            if type(self._parent) is not BaseElement:
                raise ValueError('Parent must be selenly BaseElement but it '
                             'was {}.'.format(type(self._parent)))
            else:
                parent = self._parent.element
        else:
            parent = self.__driver
                                    
        elements = strategy(criteria, parent=parent)
        if first_only: 
            if not elements:
                return None
            self._element = elements[0]
            return self._element
        return elements
    
    def __find_by_id(self, criteria, parent):
        return parent.find_elements_by_id(criteria)        
    
    def __find_by_name(self, criteria, parent):
        return parent.find_elements_by_name(criteria)     
    
    def __find_by_xpath(self, criteria, parent):
        return parent.find_elements_by_xpath(criteria)    
    
    def __find_by_css_selector(self, criteria, parent):
        return parent.find_elements_by_css_selector(criteria)        
    
    def __find_by_class_name(self, criteria, parent):
        return parent.find_elements_by_class_name(criteria)     
