from tests.testcases.test_base import TestBase
from tests.pages.home_page.google_home_page import GoogleHomePage
from tests.injection import Page
from multidict import MultiDict
from pytest_testrail.plugin import pytestrail


class Test2GoogleSearchTest(TestBase):
    google_home = Page().get_page(GoogleHomePage)

    def test_search_004(self):
        '''Test search value in Google search'''
        # validations = {}
        # pip install multidict
        validations = MultiDict()  # This support multiple duplicate keys in dictionary like KeyValuePair collection
        try:
            self.google_home.open_google()
            self.google_home.search("alo alo")
            validations.extend(self.google_home.validate_searched_value("alo alo"))
            self.google_home.search_parent("alo alo parent")
            validations.extend(self.google_home.validate_searched_value("alo alo parent "))
            self.assertNotIn(False, validations.values(), self._testMethodName)
        except Exception as ex:
            self.handle_exception(ex)

        finally:
            self.explore_validations(validations)

    def test_search_005(self):
        '''Test search value in Google search'''
        # validations = {}
        # pip install multidict
        validations = MultiDict()  # This support multiple duplicate keys in dictionary like KeyValuePair collection
        try:
            self.google_home.open_google()
            self.google_home.search("alo alo")
            validations.extend(self.google_home.validate_searched_value("alo alo"))
            self.google_home.search_parent("alo alo parent")
            validations.extend(self.google_home.validate_searched_value("alo alo parent "))
            self.assertNotIn(False, validations.values(), self._testMethodName)
        except Exception as ex:
            self.handle_exception(ex)

        finally:
            self.explore_validations(validations)
