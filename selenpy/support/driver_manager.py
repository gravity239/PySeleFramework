from selenpy.support.browsers import BrowserName
from selenpy.browser.chrome import ChromeDriver
from selenpy.browser.firefox import FirefoxDriver


class DriverManager():
    _browser_manager = None

    def __init__(self):
        self._browser_manager = {
            BrowserName.CHROME : self._start_chrome,
            BrowserName.FIREFOX: self._start_firefox
        }
    
    def start_driver(self, name, remote_host, capabilities):
        return self._browser_manager[name](remote_host, capabilities)
    
    def _start_chrome(self, remote_host, capabilities):
        return ChromeDriver().create_driver(remote_host, capabilities)
    
    def _start_firefox(self, remote_host, capabilities):
        return FirefoxDriver().create_driver(remote_host, capabilities)
