from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import ast
import os


class ChromeDriver(object):

    def create_driver(self, remote_host, browser_settings):
        options = None
        if remote_host is None:
            if browser_settings.chrome.arguments is not None:
                options = webdriver.ChromeOptions()
                options.arguments.extend(list(browser_settings.chrome.arguments.split(",")))
                if browser_settings.chrome.downloadPath is not None:
                    if browser_settings.chrome.downloadPath.find("execution") > -1:
                        download_path = os.path.dirname(os.path.abspath(__file__)) + browser_settings.chrome.downloadPath
                    else:
                        download_path = browser_settings.chrome.downloadPath

                    prefs = {'profile.default_content_setting_values.automatic_downloads': 1,
                             "download.default_directory": download_path}
                    options.add_experimental_option("prefs", prefs)
            capabilities = ast.literal_eval(browser_settings.chrome.capabilities)
            return webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                    options=options,
                                     desired_capabilities=capabilities)

        else:
            capabilities = ast.literal_eval(browser_settings.chrome.capabilities)
            return webdriver.Remote(command_executor=remote_host,
                                    desired_capabilities=capabilities)
