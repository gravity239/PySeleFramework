import time
from selenpy.common import config
from selenium.common.exceptions import StaleElementReferenceException

# def wait_for(entity, condition, timeout=5, polling=0.1):    
#     end_time = time.time() + timeout
#     while True:
#         try:
#             return condition.fn(entity)
#         except Exception as reason:
#             reason_message = getattr(reason, 'msg',
#                                      getattr(reason, 'message',
#                                              getattr(reason, 'args', '')))
#             if six.PY2:
#                 if isinstance(reason_message, unicode):
#                     reason_message = reason_message.encode('unicode-escape')
#             reason_string = '{name}: {message}'.format(name=reason.__class__.__name__, message=reason_message)
#             screen = getattr(reason, 'screen', None)
#             stacktrace = getattr(reason, 'stacktrace', None)
# 
#             if time.time() > end_time:
#                 raise TimeoutException('''
#             failed while waiting {timeout} seconds
#             to assert {condition}
#             for {entity}
# 
#             reason: {reason}'''.format(
#                     timeout=timeout,
#                     condition=condition.description(),
#                     entity=entity,
#                     reason=reason_string), screen, stacktrace)
# 
#             time.sleep(polling)
                        
# def _wait_until(condition, error, timeout=None, custom_error=None):
#         timeout = self.get_timeout(timeout)
#         if is_noney(custom_error):
#             error = error.replace('<TIMEOUT>', secs_to_timestr(timeout))
#         else:
#             error = custom_error
#         _wait_until_worker(condition, timeout, error)


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
