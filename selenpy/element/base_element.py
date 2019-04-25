from selenpy.support import browser 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenpy.common import config
from selenpy.helper.wait import wait_for


class BaseElement():
    __locator = None
    __strategies = None
    
    def __init__(self, locator):
        self.__strategies = {
            'id': self._find_by_id,
            'name': self._find_by_name,
            'xpath': self._find_by_xpath,
            'css': self._find_by_css_selector,
            'class': self._find_by_class_name
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
    
    def _find_by_id(self, criteria):
        return WebDriverWait(browser.driver(), config.timeout).until(EC.presence_of_element_located((By.ID, criteria)))
        # return browser.driver().find_element_by_id(criteria)
    
    def _find_by_name(self, criteria):
        return WebDriverWait(browser.driver(), config.timeout).until(EC.presence_of_element_located((By.NAME, criteria)))
        # return browser.driver().find_element_by_name(criteria)
    
    def _find_by_xpath(self, criteria):
        return WebDriverWait(browser.driver(), config.timeout).until(EC.presence_of_element_located((By.XPATH, criteria)))
        # return browser.driver().find_element_by_xpath(criteria)
    
    def _find_by_css_selector(self, criteria):
        return WebDriverWait(browser.driver(), config.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, criteria)))
        # return browser.driver().find_element_by_css_selector(criteria)
    
    def _find_by_class_name(self, criteria):
        return WebDriverWait(browser.driver(), config.timeout).until(EC.presence_of_element_located((By.CLASS_NAME, criteria)))
        return browser.driver().find_element_by_class_name(criteria)
    
    def is_displayed(self, timeout=None):
        return wait_for_visible(timeout)
   
    def wait_for_visible(self, timeout=None):
        if timeout == None: timeout = config.timeout            
        prefix, criteria = self.__parse_locator(self.__locator)
        return WebDriverWait(browser.driver(), timeout).until(EC.visibility_of_element_located((self.__by(prefix), criteria)))
        
    def wait_for_invisible(self, timeout=None):
        if timeout == None: timeout = config.timeout            
        prefix, criteria = self.__parse_locator(self.__locator)
        WebDriverWait(browser.driver(), timeout).until(EC.invisibility_of_element_located((self.__by(prefix), criteria)))
    
    def wait_until(self, element_condition, timeout=None, polling=None):
        if timeout is None:
            timeout = config.timeout
        if polling is None:
            polling = config.poll_during_waits
    
        return wait_for(self.find_element(), element_condition, timeout, polling)
