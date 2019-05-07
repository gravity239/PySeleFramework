import sys

from selenpy.element.locator_loader import LocatorLoader
from selenpy.element.locator_loader import BaseLocator

class PageBase(LocatorLoader):

    def __init__(self, derived_class_name):
        LocatorLoader.__init__(self, derived_class_name)
        self.init_elements()

    def create_locator(self, locator_name):
        return BaseLocator.create_locator(self.locators, locator_name)

    def init_elements(self):
        pass

    def log(self, message):
        from datetime import datetime
        str_time = datetime.now().strftime('%m/%d/%Y-%H:%M:%S')
        print(
            "[{}][{}] {}".format(str_time, self.__class__.__name__ + " - " + sys._getframe(1).f_code.co_name, message))
