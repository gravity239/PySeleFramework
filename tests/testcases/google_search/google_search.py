from tests.testcases.test_base import TestBase
from tests.pages.home_page.google_home_page import GoogleHomePage
from tests.injection import Page


class GoogleSearchTest(TestBase):

    google_home = Page.get_page(GoogleHomePage)


    def test_search_001(self):
        self.google_home.open_google()
        self.google_home.search("hello selenium")
