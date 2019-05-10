import os
import sys
from selenium.webdriver.common.by import By
from selenpy.support import factory

class LocatorLoader(object):
    '''
    Load locators for a screeen from json file.
    
    The derived class name must be used as the JSON file name so that this class can use it 
    to detect the JSON file in the location 'src/execution/locator/' and load its content.
    
    For example: for a Page Object, named 'Home' and derived this class, we must create a file Home.json
    in folder src/execution/locator/ and put all locators of Home screen in this file with following format:
    '''

    locators = {}
    def __init__(self, derived_class_name):
        if derived_class_name:
            self.__load_locator(derived_class_name)

    def create_locator(self, locator_name):
        return BaseLocator.create_locator(self.locators, locator_name)

    def __load_locator(self, derived_class_name):
        if factory.get_current_run_mode() is None and '--run-mode=mobile' in sys.argv:
            current_run_mode = "mobile"
        elif factory.get_current_run_mode() is None and '--run-mode=mobile' not in sys.argv:
            current_run_mode = "desktop"
        else:
            current_run_mode = factory.get_current_run_mode()
        import tests
        file_path = os.path.join(
            os.path.dirname(tests.__file__),
            'locator',
            current_run_mode,
            '{0}.json'.format(derived_class_name))

        import json
        with open(file_path) as handle:
            file_dict = json.loads(handle.read())
            try:
                if factory.get_current_browser_name().lower() == "firefox":
                    self.locators = file_dict["firefox"]
                elif factory.get_current_browser_name().lower() == "native":
                    self.locators = file_dict["native"]
                else:
                    self.locators = file_dict["default"]
            except:
                self.locators = file_dict["default"] #in case we don't need define locator for multi browser

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

    def value(self):
        return self._value
