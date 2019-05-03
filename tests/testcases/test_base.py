import unittest
import pytest
import os
from selenpy.support import browser
from selenpy.support import browser

import logging


class TestBase(unittest.TestCase):

    @pytest.fixture(scope="session", autouse=True)
    def setup(self):
        logging.info("Starting the test on " + str(pytest.browser_name))
        browser_settings = browser.get_browser_settings(pytest.browser_config_file)
        browser.start_driver(pytest.browser_name, pytest.remote_host, browser_settings)
        # browser.maximize_browser() - this doesn't work with android chrome
        # Close all browsers when tests have been finished
        yield        
        browser.quit_all_browsers()        
