import os

from selenium.webdriver.common.by import By
from selenpy.support import factory

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
        return BaseLocator.create_locator(self.locators, locator_name)

    def __load_locator(self, derived_class_name):
        import execution
        file_path = os.path.join(
            os.path.dirname(execution.__file__),
            'locator',
            factory.get_current_run_mode(),
            '{0}.json'.format(derived_class_name))

        import json
        with open(file_path) as handle:
            file_dict = json.loads(handle.read())
            self.locators = file_dict["default"]

class BaseLocator(object):

    @staticmethod
    def create_locator(locator_dict, name):
        try:
            return BaseLocator(locator_dict, name).value()
        except Exception as ex:
            print("Warning: Cannot find the locator value of '{0}'".format(name))
            print(ex)
            return None

    def __init__(self, locator_dict, name):
        self._value = locator_dict[name]['value']
        # tp = locator_dict[name]["type"]
        # if tp == 'xpath':
        #     self._by = By.XPATH
        # elif tp == 'class-name':
        #     self._by = By.CLASS_NAME
        # elif tp == 'css':
        #     self._by = By.CSS_SELECTOR
        # elif tp == 'id':
        #     self._by = By.ID
        # elif tp == 'name':
        #     self._by = By.NAME
        # elif tp == 'tag-name':
        #     self._by = By.TAG_NAME
        # elif tp == 'link-text':
        #     self._by = By.LINK_TEXT
        # elif tp == 'partial-link-text':
        #     self._by = By.PARTIAL_LINK_TEXT
        # else:
        #     self._by = By.XPATH
        # self._value = locator_dict[name]['value']

    # def by(self):
    #     return self._by
    #
    def value(self):
        return self._value
