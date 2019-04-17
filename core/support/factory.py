from browser.chrome import ChromeDriver
from support.browsers import BrowserName
from support.driver import SharedWebDriver

__driver = {}
__shared_web_driver = None


def __start_chrome():
    return ChromeDriver().create_driver()


def start_driver(name, driver_key="default"):
    __shared_web_driver = SharedWebDriver()
    driver = __get_driver(name)   
    __shared_web_driver.driver = driver
    __driver[driver_key] = __shared_web_driver
    Key.current = driver_key


def __get_driver(name):
    if name == BrowserName.CHROME:
        return __start_chrome()

   
def _get_shared_driver():
    return __driver[Key.current].driver


def maximize_browser():
    _get_shared_driver().maximize_window()

        
def navigate(url):
    _get_shared_driver().get(url)    


def switch_to_driver(driver_key="default"):
    Key.current = driver_key


def close_browser():
    if Key.current in __driver: del __driver[Key.current]
    _get_shared_driver().close()    


def close_all_browsers():
    for key in __driver: __driver[key].driver.quit()
    __driver.clear()


class Key:
    current = "default"