import unittest
import pytest

from support.factory import start_driver, maximize_browser, close_all_browsers, navigate


class TestBase(unittest.TestCase):
    
    @pytest.fixture(scope="session", autouse=True)
    def setup(self):        
        start_driver("chrome")
        maximize_browser()
        navigate("https://google.com")    
        
        # Close all browsers when tests have been finished
        yield        
        close_all_browsers()        
