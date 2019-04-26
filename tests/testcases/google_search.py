from tests.testcases.test_base import TestBase
from tests.pages.google_home_page import GoogleHomePage


class GoogleSearchTest(TestBase):
    
    google_home = GoogleHomePage()
    
    def test_search_001(self):
        self.google_home.open_google()
        self.google_home.search("hello selenium")
