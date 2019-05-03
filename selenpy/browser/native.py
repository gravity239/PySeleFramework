import ast

from appium import webdriver


class NativeDriver(object):
    def create_driver(self, remote_host, browser_settings):
        capabilities = ast.literal_eval(browser_settings.native.capabilities)

        return webdriver.Remote(command_executor=remote_host,
                                desired_capabilities=capabilities())
