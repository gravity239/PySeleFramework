from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import os
import ast


class FirefoxDriver(object):

    def create_driver(self, remote_host, browser_settings):
        options = None
        profile = None
        if remote_host is None:
            if browser_settings.firefox.arguments is not None:
                options = webdriver.FirefoxOptions()
                options.arguments.extend(list(browser_settings.firefox.arguments.split(",")))
            if browser_settings.firefox.downloadPath is not None:
                profile = webdriver.FirefoxProfile()
                if browser_settings.firefox.downloadPath.find("execution") > -1:
                    download_path = os.path.dirname(os.path.abspath(__file__)) + browser_settings.firefox.downloadPath
                else:
                    download_path = browser_settings.firefox.downloadPath
                profile.set_preference('browser.download.folderList',
                                           2)  # # 0 means to download to the desktop, 1 means to download to the default "Downloads" directory, 2 means to use custom location
                profile.set_preference('browser.download.manager.showWhenStarting', False)
                profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                                           'image/gif;image/png;image/jpeg;image/jpg;application/x-compressed;application/x-zip-compressed;application/zip;multipart/x-zip')  # type of file to download
                profile.set_preference('browser.download.dir', download_path)
                profile.update_preferences()
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                     options=options, firefox_profile=profile)
        else:
            capabilities = ast.literal_eval(browser_settings.firefox.capabilities)
            return webdriver.Remote(command_executor=remote_host,
                                    desired_capabilities=capabilities)
