from __future__ import print_function

import logging

log = logging.getLogger()
logging.basicConfig(level=logging.INFO)

print(log.handlers[0].formatter._fmt)

log.addHandler(logging.StreamHandler())

print(log.handlers[1].formatter)

formatter = logging.Formatter('foo bar baz: %(message)s')

log.handlers[1].setFormatter(formatter)

print('# Now the logging')
log.info('say hello')
