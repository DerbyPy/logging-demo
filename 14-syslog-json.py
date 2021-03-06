from __future__ import print_function

import logging
from logging.handlers import SysLogHandler

from pythonjsonlogger import jsonlogger

json_format_str = '%(asctime)s %(pathname) %(funcName) %(lineno) %(message) %(levelname)' \
                  ' %(name)s %(process) %(processName) %(message)'
json_formatter = jsonlogger.JsonFormatter(json_format_str, prefix='logging-demo-14 ')

handler = SysLogHandler('/dev/log')
handler.setFormatter(json_formatter)

log = logging.getLogger()
log.setLevel(logging.INFO)
log.addHandler(handler)

log.info('hello world')

try:
    5 / 0
except Exception:
    log.exception('division error')
    pass
