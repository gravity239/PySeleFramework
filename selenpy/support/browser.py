
from selenpy.support import factory
from selenpy.common import config
from selenpy.helper.wait import wait_for


def get_driver():
    return factory.get_shared_driver()


def maximize_browser():
    get_driver().maximize_window()

        
def open_url(url):
    get_driver().get(url)    


def switch_to_driver(driver_key="default"):
    factory.switch_to_driver(driver_key)


def close_browser():
    factory.close_browser()


def quit_all_browsers():
    factory.quit_all_browsers()


def start_driver(name, remote_host, key="default"):
    factory.start_driver(name, remote_host, key)


def wait_until(webdriver_condition, timeout=None, polling=None):
    if timeout is None:
        timeout = config.timeout
    if polling is None:
        polling = config.poll_during_waits

    return wait_for(get_driver(), webdriver_condition, timeout, polling)
