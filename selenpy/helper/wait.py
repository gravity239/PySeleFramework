import six
import time
from selenium.common.exceptions import TimeoutException


def wait_for(entity, condition, timeout=5, polling=0.1):    
    end_time = time.time() + timeout
    while True:
        try:
            return condition.fn(entity)
        except Exception as reason:
            reason_message = getattr(reason, 'msg',
                                     getattr(reason, 'message',
                                             getattr(reason, 'args', '')))
            if six.PY2:
                if isinstance(reason_message, unicode):
                    reason_message = reason_message.encode('unicode-escape')
            reason_string = '{name}: {message}'.format(name=reason.__class__.__name__, message=reason_message)
            screen = getattr(reason, 'screen', None)
            stacktrace = getattr(reason, 'stacktrace', None)

            if time.time() > end_time:
                raise TimeoutException('''
            failed while waiting {timeout} seconds
            to assert {condition}
            for {entity}

            reason: {reason}'''.format(
                    timeout=timeout,
                    condition=condition.description(),
                    entity=entity,
                    reason=reason_string), screen, stacktrace)

            time.sleep(polling)
            
