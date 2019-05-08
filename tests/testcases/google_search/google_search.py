from tests.testcases.test_base import TestBase
from tests.pages.home_page.google_home_page import GoogleHomePage
from tests.injection import Page
from multidict import MultiDict


class GoogleSearchTest(TestBase):
    google_home = Page.get_page(GoogleHomePage)

    def test_search_001(self):
        '''Test search value in Google search'''
        # validations = {}
        #pip install multidict
        validations = MultiDict() # This support multiple duplicate keys in dictionary like KeyValuePair collection
        try:
            self.google_home.open_google()
            self.google_home.search("hello selenium")
            validations.extend(self.google_home.validate_searched_value("hello selenium 1"))
            self.google_home.search_parent("hello selenium parent")
            validations.extend(self.google_home.validate_searched_value("hello selenium parent"))
            self.assertNotIn(False, validations.values(), self._testMethodName)
        except Exception as ex:
            self.handle_exception(ex)

        finally:
            self.explore_validations(validations)
