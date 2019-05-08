import time
from selenpy.common import config
from selenium.common.exceptions import StaleElementReferenceException


def wait_until(condition, error=None, timeout=None, polling=None):
        if timeout is None:
            timeout = config.timeout
        if polling is None:
            polling = config.poll_during_waits
        max_time = time.time() + timeout
        not_found = None
        while time.time() < max_time:
            try:
                if condition():
                    return            
            except StaleElementReferenceException as err:                
                not_found = err
            else:
                not_found = None
            time.sleep(polling)
        raise AssertionError(not_found or error)            
