from support.browsers import BrowserName
from browser.chrome import ChromeDriver


class DriverManager():
    _browser_manager = None

    def __init__(self):
        self._browser_manager = {
            BrowserName.CHROME : self._start_chrome,
            BrowserName.FIREFOX: self._start_firefox
        }
    
    def start_driver(self, name, capabilities):
        return self._browser_manager[name](capabilities)
    
    def _start_chrome(self, capabilities):
        return ChromeDriver().create_driver(capabilities)
    
    def _start_firefox(self, capabilities):
        return ChromeDriver().create_driver(capabilities)
