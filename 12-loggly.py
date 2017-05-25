from __future__ import print_function

import logging
from logging.handlers import HTTPHandler

url = '/inputs/c92a2ed9-1256-4d99-a357-7f78071b574a/tag/http/'
handler = HTTPHandler('logs-01.loggly.com', url, 'POST')

log = logging.getLogger()
log.setLevel(logging.INFO)
log.addHandler(handler)

log.info('hello world')

try:
    5 / 0
except Exception:
    log.exception('division error')
    pass
