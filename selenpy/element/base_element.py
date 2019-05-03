import os

from selenpy.support import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenpy.common import config
from selenpy.helper.wait import wait_for
from pywinauto.findwindows import find_element


class BaseElement():
    __locator = None
    __strategies = None
    
    def __init__(self, locator, **kwargs):
        self.__strategies = {
            'id': self._find_by_id,
            'name': self._find_by_name,
            'xpath': self._find_by_xpath,
            'css': self._find_by_css_selector,
            'class': self._find_by_class_name
        }
        self.__locator = locator
        self.__parent = kwargs.get('parent')
        # self.__new_locator = locator.value().format(kwargs.get('dynamic_value'))

    @property
    def _driver(self):
        return browser.get_driver()

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
        return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_element_located((By.ID, criteria)))        
    
    def _find_by_name(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_element_located((By.NAME, criteria)))        
    
    def _find_by_xpath(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_element_located((By.XPATH, criteria)))       
    
    def _find_by_css_selector(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, criteria)))        
    
    def _find_by_class_name(self, criteria):
        return WebDriverWait(self._driver, config.timeout).until(EC.presence_of_element_located((By.CLASS_NAME, criteria)))        
    
    def is_displayed(self, timeout=None):
        return self.wait_for_visible(timeout)
    
    def is_enabled(self):
        return find_element().is_enabled()
    
    def is_selected(self):
        return find_element().is_selected()
   
    def wait_for_visible(self, timeout=None):
        if timeout == None: timeout = config.timeout            
        prefix, criteria = self.__parse_locator(self.__locator)
        return WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located((self.__by(prefix), criteria)))
        
    def wait_for_invisible(self, timeout=None):
        if timeout == None: timeout = config.timeout            
        prefix, criteria = self.__parse_locator(self.__locator)
        WebDriverWait(self._driver, timeout).until(EC.invisibility_of_element_located((self.__by(prefix), criteria)))
    
    def wait_until(self, element_condition, timeout=None, polling=None):
        if timeout is None:
            timeout = config.timeout
        if polling is None:
            polling = config.poll_during_waits
    
        return wait_for(self.find_element(), element_condition, timeout, polling)


class LocatorLoader(object):
    '''
    Load locators for a screeen from json file.

    The derived class name must be used as the JSON file name so that this class can use it
    to detect the JSON file in the location 'src/execution/locator/' and load its content.

    For example: for a Page Object, named 'Home' and derived this class, we must create a file Home.json
    in folder src/execution/locator/ and put all locators of Home screen in this file with following format:
    {
        "default":{
            "_btnLogOutLocator":{
                "type":"xpath",
                "value":"//div[@dir = 'auto' and text()='Log Out']"
            }
        }
    }
    '''

    locators = {}

    def __init__(self, derived_class_name):
        if derived_class_name:
            self.__load_locator(derived_class_name)

    def create_locator(self, locator_name):
        return BaseLocator.createLocator(self.locators, locator_name)

    def __load_locator(self, derived_class_name):
        import execution
        file_path = os.path.join(
            os.path.dirname(execution.__file__),
            'locator',
            DriverManager._run_mode,
            '{0}.json'.format(derived_class_name))

        import json
        with open(file_path) as handle:
            file_dict = json.loads(handle.read())
            self.locators = file_dict["default"]
            # target_key = DriverManager._run_target
            # # if target_key in file_dict:
            #     self.locators = dict(list(file_dict["default"].items())) # + list(file_dict[target_key].items())) # { file_dict["default"], file_dict[target_key] }


class BaseLocator(object):

    @staticmethod
    def createLocator(locatorDict, name):
        try:
            return BaseLocator(locatorDict, name)
        except Exception as ex:
            print("Warning: Cannot find the locator value of '{0}'".format(name))
            print(ex)
            return None

    def __init__(self, locatorDict, name):
        tp = locatorDict[name]["type"]
        if tp == 'xpath':
            self._by = By.XPATH
        elif tp == 'class-name':
            self._by = By.CLASS_NAME
        elif tp == 'css':
            self._by = By.CSS_SELECTOR
        elif tp == 'id':
            self._by = By.ID
        elif tp == 'name':
            self._by = By.NAME
        elif tp == 'tag-name':
            self._by = By.TAG_NAME
        elif tp == 'link-text':
            self._by = By.LINK_TEXT
        elif tp == 'partial-link-text':
            self._by = By.PARTIAL_LINK_TEXT
        else:
            self._by = By.XPATH
        self._value = locatorDict[name]['value']

    def by(self):
        return self._by

    def value(self):
        return self._value
