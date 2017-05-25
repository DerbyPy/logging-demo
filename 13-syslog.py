from __future__ import print_function

import logging
from logging.handlers import SysLogHandler

format_str = 'logging-demo-13 %(levelname)s %(name)s %(message)s'
formatter = logging.Formatter(format_str)

handler = SysLogHandler('/dev/log')
handler.setFormatter(formatter)

log = logging.getLogger()
log.setLevel(logging.INFO)
log.addHandler(handler)

log.info('hello world')

try:
    5 / 0
except Exception:
    log.exception('division error')
    pass
