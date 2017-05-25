from __future__ import print_function

import logging


# This is the "root" logger
log = logging.getLogger()

log.error('error 1')

print('handlers', log.handlers)

# Have to call basicConfig() explicitly now
logging.basicConfig()

print('handlers', log.handlers)

log.debug('lots of detail')
log.info('some info')
log.warning('a warning')

log.setLevel(logging.INFO)

log.debug('lots of detail 2')
log.info('some info 2')
