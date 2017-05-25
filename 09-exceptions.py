from __future__ import print_function

import logging

log = logging.getLogger()
logging.basicConfig(filename='exceptions.log')

try:
    5 / 0
except Exception:
    log.exception('trying to divide failed')
    pass
