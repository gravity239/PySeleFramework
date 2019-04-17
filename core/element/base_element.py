from support.factory import _get_shared_driver 


class BaseElement():
    __locator = None
    __strategies = None
    
    def __init__(self, locator):
        self.__strategies = {
            'id': self._find_by_id,
            'name': self._find_by_name,
            'xpath': self._find_by_xpath,
            'css': self._find_by_css_selector,
            'class': self._find_by_class_name,
            'default': self._find_by_xpath
        }
        self.__locator = locator
    
    def find_element(self):
        prefix, criteria = self.__parse_locator(self.__locator)
        strategy = self.__strategies[prefix]
        return strategy(criteria)
    
    def click(self):
        self.find_element().click()
        
    def send_keys(self, *value):
        self.find_element().send_keys(value)
    
    def __parse_locator(self, locator):
        if locator.startswith(('//', '(//')):
            return 'xpath', locator
        index = self.__get_locator_separator_index(locator)
        if index != -1:
            prefix = locator[:index].strip()
            if prefix in self.__strategies:
                return prefix, locator[index + 1:].lstrip()
        return 'default', locator
    
    def __get_locator_separator_index(self, locator):
        if '=' not in locator:
            return locator.find(':')
        if ':' not in locator:
            return locator.find('=')
        return min(locator.find('='), locator.find(':'))
    
    def _find_by_id(self, criteria):
        return _get_shared_driver().find_element_by_id(criteria)
    
    def _find_by_name(self, criteria):
        return _get_shared_driver().find_element_by_name(criteria)
    
    def _find_by_xpath(self, criteria):
        return _get_shared_driver().find_element_by_xpath(criteria)
    
    def _find_by_css_selector(self, criteria):
        return _get_shared_driver().find_element_by_css_selector(criteria)
    
    def _find_by_class_name(self, criteria):
        return _get_shared_driver().find_element_by_class_name(criteria)
   
