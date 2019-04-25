import itertools
import os
import time

from selenpy.common.environment import *
from selenpy.common.helpers import env

timeout = int(env(SELENPY_TIMEOUT, 5))
poll_during_waits = float(env(SELENPY_POLL_DURING_WAITS, 0.5))

