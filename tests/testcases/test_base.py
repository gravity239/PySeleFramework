import unittest
import pytest

from selenpy.support import browser
import logging


class TestBase(unittest.TestCase):

    @pytest.fixture(scope="session", autouse=True)
    def setup(self):
        logging.info("Starting the test on " + str(pytest.browser_name))                
        browser.start_driver(pytest.browser_name, pytest.remote_host)
        browser.maximize_browser()
        # Close all browsers when tests have been finished
        yield        
        browser.quit_all_browsers()        
