from tests.testcases.test_base import TestBase
from tests.pages.home_page.google_home_page import GoogleHomePage
from tests.injection import Page
from multidict import MultiDict
from selenpy.support import factory

class GoogleSearchTest(TestBase):
    google_home = Page().get_page(GoogleHomePage)

    def test_search_001(self):
        '''Test search value in Google search'''
        # validations = {}
        #pip install multidict
        validations = MultiDict() # This support multiple duplicate keys in dictionary like KeyValuePair collection
        try:
            self.start_driver("chrome", None, "tests/config/browser_setting_default.cfg", "desktop", "second")
            self.switch_driver("default")
            self.google_home.open_google()
            self.google_home.search("hello selenium")
            validations.extend(self.google_home.validate_searched_value("hello selenium 1"))

            self.switch_driver("second")
            self.google_home.open_google()
            self.google_home.search_parent("hello selenium parent")
            validations.extend(self.google_home.validate_searched_value("hello selenium parent"))
            self.assertNotIn(False, validations.values(), self._testMethodName)
        except Exception as ex:
            self.handle_exception(ex)

        finally:
            self.explore_validations(validations)

    def test_search_002(self):
        '''Test search value in Google search in desktop and mobile chrome'''
        # validations = {}
        #pip install multidict
        validations = MultiDict() # This support multiple duplicate keys in dictionary like KeyValuePair collection
        try:
            self.start_driver("chrome", None, "tests/config/browser_setting_android.cfg", "mobile", "second")
            self.switch_driver("default")
            self.google_home_desktop = Page().get_page(GoogleHomePage) # Can't find any solution to avoid duplicate code at the moment
            self.google_home_desktop.open_google()
            self.google_home_desktop.search_parent("hello selenium parent")
            validations.extend(self.google_home_desktop.validate_searched_value("hello selenium parent"))

            self.switch_driver("second")
            self.google_home_mobile = Page().get_page(GoogleHomePage) # Can't find any solution to avoid duplicate code at the moment
            self.google_home_mobile.open_google()
            self.google_home_mobile.search("hello selenium")
            validations.extend(self.google_home_mobile.validate_searched_value("hello selenium"))

            self.assertNotIn(False, validations.values(), self._testMethodName)
        except Exception as ex:
            self.handle_exception(ex)

        finally:
            self.explore_validations(validations)
