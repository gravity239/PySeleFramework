from selenpy.support import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenpy.common import config
from selenpy.helper.wait import wait_for
from selenpy.support.conditions import be


class BaseElement():
    _locator = None
    _strategies = None
    _dymanic_locator = None
    
    def __init__(self, locator):
        self._strategies = {
            'id': self._find_by_id,
            'name': self._find_by_name,
            'xpath': self._find_by_xpath,
            'css': self._find_by_css_selector,
            'class': self._find_by_class_name
        }
        self._locator = locator
        self._dymanic_locator = locator
    
    def format(self, *args):
        self._locator = self._dymanic_locator % (args)

    @property
    def _driver(self):
        return browser.get_driver()
    
    @property
    def text(self):
        return self.find_element().text
    
    @property
    def tag_name(self):
        return self.find_element().tag_name
    
    def get_attribute(self, name):
        return self.find_element().get_attribute(name)

    def _find(self, first_only=True):
        prefix, criteria = self.__parse_locator(self._locator)
        strategy = self._strategies[prefix]
        elements = strategy(criteria)
        if first_only: 
            return elements[0]
        return elements

    def find_element(self):
        return self._find()
    
    def find_elements(self):
        return self._find(False)
    
    def click(self):
        element = self.find_element()
        # Wait until element is enabled before clicking
        wait_for(element, be.enabled, config.timeout, config.poll_during_waits)
        element.click()
        
    def send_keys(self, *value):
        self.find_element().send_keys(value)
    
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
    
    def _find_by_id(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_all_elements_located((By.ID, criteria)))        
    
    def _find_by_name(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_all_elements_located((By.NAME, criteria)))        
    
    def _find_by_xpath(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_all_elements_located((By.XPATH, criteria)))       
    
    def _find_by_css_selector(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, criteria)))        
    
    def _find_by_class_name(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_all_elements_located((By.CLASS_NAME, criteria)))     
            
    def is_displayed(self, timeout=None):
        try:
            return self.wait_for_visible(timeout)
        except TimeoutException:
            return False
    
    def is_enabled(self):
        return self.find_element().is_enabled()
    
    def is_selected(self):
        return self.find_element().is_selected()
   
    def wait_for_visible(self, timeout=None):
        if timeout == None: timeout = config.timeout            
        prefix, criteria = self.__parse_locator(self._locator)
        return WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located((self.__by(prefix), criteria)))
        
    def wait_for_invisible(self, timeout=None):
        if timeout == None: timeout = config.timeout            
        prefix, criteria = self.__parse_locator(self._locator)
        WebDriverWait(self._driver, timeout).until(EC.invisibility_of_element_located((self.__by(prefix), criteria)))    
    
    def wait_until(self, element_condition, timeout=None, polling=None):
        if timeout is None:
            timeout = config.timeout
        if polling is None:
            polling = config.poll_during_waits
    
        return wait_for(self.find_element(), element_condition, timeout, polling)
