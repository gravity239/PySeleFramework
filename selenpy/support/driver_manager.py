from selenpy.support.browsers import BrowserName
from selenpy.browser.chrome import ChromeDriver
from selenpy.browser.firefox import FirefoxDriver
from selenpy.browser.native import NativeDriver


class DriverManager():    

    def __init__(self):
        self._browser_manager = {
            BrowserName.CHROME: self._start_chrome,
            BrowserName.FIREFOX: self._start_firefox,
            BrowserName.NATIVE: self._start_native
        }

    def start_driver(self, name, remote_host, browser_settings):
        return self._browser_manager[name](remote_host, browser_settings)

    def _start_chrome(self, remote_host, browser_settings):
        return ChromeDriver().create_driver(remote_host, browser_settings)

    def _start_firefox(self, remote_host, browser_settings):
        return FirefoxDriver().create_driver(remote_host, browser_settings)

    def _start_native(self, remote_host, browser_settings):
        return NativeDriver().create_driver(remote_host, browser_settings)
