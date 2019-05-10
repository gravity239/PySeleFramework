from tests.testcases.test_base import TestBase
from tests.pages.home_page.google_home_page import GoogleHomePage
from tests.injection import Page
from multidict import MultiDict
from pytest_testrail.plugin import pytestrail


class GoogleSearchTest(TestBase):
    google_home = Page().get_page(GoogleHomePage)

    @pytestrail.case('C3')
    def test_search_001(self):
        '''Test search value in Google search'''
        # validations = {}
        # pip install multidict
        validations = MultiDict()  # This support multiple duplicate keys in dictionary like KeyValuePair collection
        try:
            self.google_home.open_google()
            self.google_home.search("hello selenium")
            validations.extend(self.google_home.validate_searched_value("hello selenium"))
            self.google_home.search_parent("hello selenium parent")
            validations.extend(self.google_home.validate_searched_value("hello selenium parent"))
            self.assertNotIn(False, validations.values(), self._testMethodName)
        except Exception as ex:
            self.handle_exception(ex)

        finally:
            self.explore_validations(validations)


    # def test_search_002(self):
    #     '''Test search value in Google search in desktop and mobile chrome'''
    #     # validations = {}
    #     # pip install multidict
    #     validations = MultiDict()  # This support multiple duplicate keys in dictionary like KeyValuePair collection
    #     try:
    #         self.start_driver("chrome", None, "tests/config/browser_setting_android.cfg", "mobile",
    #                           "second")  # you just need connect your mobile to computer, no need Appium installed
    #         self.start_driver("firefox", None, "tests/config/browser_setting_default.cfg", "desktop", "third")
    #
    #         self.switch_driver("default")
    #         self.google_home_desktop = Page().get_page(
    #             GoogleHomePage)
    #         self.google_home_desktop.open_google()
    #         self.google_home_desktop.search_parent("hello selenium parent")
    #         validations.extend(self.google_home_desktop.validate_searched_value("hello selenium parent"))
    #
    #         self.switch_driver("second")
    #         self.google_home_mobile = Page().get_page(
    #             GoogleHomePage)
    #         self.google_home_mobile.open_google()
    #         self.google_home_mobile.search("hello selenium")
    #         validations.extend(self.google_home_mobile.validate_searched_value("hello selenium"))
    #
    #         self.switch_driver("third")
    #         self.google_home_desktop.open_google()
    #         self.google_home_desktop.search_parent("hello selenium parent by firefox")
    #         validations.extend(self.google_home_desktop.validate_searched_value("hello selenium parent by firefox"))
    #         self.assertNotIn(False, validations.values(), self._testMethodName)
    #     except Exception as ex:
    #         self.handle_exception(ex)
    #
    #     finally:
    #         self.explore_validations(validations)

    @pytestrail.case('C4')
    def test_search_003(self):
        '''This is a alternative way to avoid duplicate code as test_search_002'''
        instance_dict = {
            GoogleHomePage: self.google_home}  # use for re-initialize instances when we switch driver. No need to use this in case we just use one driver
        #         # pip install multidict
        validations = MultiDict()  # This support multiple duplicate keys in dictionary like KeyValuePair collection
        try:
            self.start_driver("chrome", None, "tests/config/browser_setting_android.cfg", "mobile",
                              "second") # you just need connect your mobile to computer, no need Appium installed or change the browser setting to default so that it will create a new chorme on desktop
            self.start_driver("firefox", None, "tests/config/browser_setting_default.cfg", "desktop", "third")

            self.switch_driver("default", instance_dict)
            instance_dict[GoogleHomePage].open_google()
            instance_dict[GoogleHomePage].search_parent("hello selenium parent")
            validations.extend(instance_dict[GoogleHomePage].validate_searched_value("hello selenium parent"))

            self.switch_driver("second", instance_dict)
            instance_dict[
                GoogleHomePage].open_google()  # this should open Bing website instead of google due to the overrided method
            instance_dict[GoogleHomePage].search("hello selenium")
            validations.extend(instance_dict[GoogleHomePage].validate_searched_value("hello selenium"))

            self.switch_driver("third", instance_dict)
            instance_dict[GoogleHomePage].open_google()
            instance_dict[GoogleHomePage].search_parent("hello selenium parent")
            validations.extend(instance_dict[GoogleHomePage].validate_searched_value("hello selenium parent"))

            self.assertNotIn(False, validations.values(), self._testMethodName)
        except Exception as ex:
            self.handle_exception(ex)

        finally:
            self.explore_validations(validations)
