import sys
import unittest
import allure
import pytest
from selenpy.support import browser
from tests.common.utilities import Utilities
import logging
from tests.injection import Page
import json
import ast


class TestBase(unittest.TestCase):

    @pytest.fixture(scope="session", autouse=True)
    def setup(self):
        logging.info("Starting the test on " + str(pytest.browser_name))
        browser.start_driver(pytest.browser_name, pytest.remote_host, pytest.browser_config_file, pytest.run_mode)
        # browser.maximize_browser() - this doesn't work with android chrome
        # Close all browsers when tests have been finished
        yield
        browser.quit_all_browsers()

    def start_driver(self, name, remote_host, browser_config_file, driver_key="default", run_mode="desktop"):
        return browser.start_driver(name, remote_host, browser_config_file, driver_key, run_mode)

    def handle_exception(self, exception):
        # print(exception)
        if not isinstance(exception, AssertionError):
            Utilities.attach_screenshot_for_allure_report()

        raise exception

    def switch_driver(self, driver_key="default", instance_dict=None):
        browser.switch_to_driver(driver_key)
        if instance_dict is not None:
            for key in instance_dict:
                instance_dict[key] = Page().get_page(key)

        # if browser.is_run_mode_changeed(driver_key) is True:
        #     parent_classes = Page().get_parent_classes()
        #     for i in range(len(parent_classes)):
        #         for obj in gc.get_referents():
        #             if isinstance(obj, parent_classes[i]):
        #                 object_name = str(id(obj))
        #                 self.obj = Page().get_page(parent_classes[i])
        #                 # self.google_home = obj

    def assertNotIn(self, member, container, msg):
        try:
            unittest.TestCase.assertNotIn(self, member, container)
        except:
            self.fail(msg)


    @allure.step
    def explore_validations(self, validations, exception_tuple, test_method):
        from selenpy.helper import config_file_parser
        bug_config = config_file_parser.parseConfigFile("tests/bugs/bug_config.cfg")
        if bug_config.jira_support == "True":
            from selenpy.common.jira_issue_reporter_handler import JiraIssueReporterHandler
            jira_helper = JiraIssueReporterHandler(bug_config.jira.url, bug_config.jira.username,
                                                   bug_config.jira.api_token,
                                                   bug_config.jira.projectkey)
            bug_list = ast.literal_eval(bug_config.bug_list)
            if exception_tuple[0] is not AssertionError and exception_tuple[0] is not None:
                pass
            else:
                if False in validations.values():
                    if test_method not in bug_list or bug_list[test_method] is None:
                        jira_helper.create_new_bug(test_method, "Assertion error - " + str(validations))
                    else:
                        if jira_helper.get_issue_status(bug_list[test_method]) != "To Do":
                            jira_helper.mark_issue_status(bug_list[test_method], "To Do")
                        jira_helper.add_bug_comment(bug_list[test_method], "This issue is {color:red}*HAPPENING*{color}")
                else:
                    if test_method in bug_list:
                        if jira_helper.get_issue_status(bug_list[test_method]) != "Done":
                            jira_helper.mark_issue_status(bug_list[test_method], "Done")
                            jira_helper.add_bug_comment(bug_list[test_method], "This issue is {color:green}*Fixed*{color}")



