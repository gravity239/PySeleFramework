
from selenpy.support import factory
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


def start_driver(name, remote_host, key="default"):
    factory.start_driver(name, remote_host, key)

    
def select_main_window():
    handles = get_driver().window_handles
    get_driver().switch_to.window(handles[0])


def wait_for_title_contains(value, timeout=None):
    wait_until(lambda: value in get_title() , "Title '%s' did not display after after <TIMEOUT>." % value, timeout)

