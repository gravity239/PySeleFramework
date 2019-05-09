from selenpy.support.driver_manager import DriverManager
from selenpy.support.driver import SharedWebDriver

__driver = {}
__shared_web_driver = None
__driver_mode = {}

def start_driver(name, remote_host, browser_settings, run_mode="desktop", driver_key="default"):
    __shared_web_driver = SharedWebDriver()
    __shared_web_driver.driver = DriverManager().start_driver(name, remote_host, browser_settings)
    __driver[driver_key] = __shared_web_driver
    __driver_mode[driver_key] = run_mode
    Key.current = driver_key
    RunMode.current_run_mode = run_mode

def get_shared_driver():
    return __driver[Key.current].driver


def switch_to_driver(driver_key="default"):
    Key.current = driver_key
    set_current_run_mode(__driver_mode[driver_key])

def close_browser():
    get_shared_driver().close()


def quit_all_browsers():
    for key in __driver: __driver[key].driver.quit()
    __driver.clear()


def get_current_run_mode():
    return RunMode.current_run_mode


def set_current_run_mode(run_mode):
    RunMode.current_run_mode = run_mode


class Key:
    current = "default"

class RunMode:
    current_run_mode = None
