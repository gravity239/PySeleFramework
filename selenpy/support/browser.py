
from selenpy.support import factory
from selenpy.helper import config_file_parser
from selenpy.helper.wait import wait_until


def get_driver():
    return factory.get_shared_driver()


def get_title():
    return get_driver().title


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


def start_driver(name, remote_host, browser_config_file= None, run_mode="desktop", key="default"):
    browser_settings = get_browser_settings(browser_config_file)
    factory.start_driver(name, remote_host, browser_settings, run_mode, key)

def select_main_window():
    handles = get_driver().window_handles
    get_driver().switch_to.window(handles[0])


def get_browser_settings(file_path):
    if file_path is not None:
        return config_file_parser.parseConfigFile(file_path)
    else:
        return None

def wait_for_title_contains(value, timeout=None):
    wait_until(lambda: value in get_title() , "Title '%s' did not display after after <TIMEOUT>." % value, timeout)
