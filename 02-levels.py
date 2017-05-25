from __future__ import print_function

import logging

logging.basicConfig(level=logging.INFO)

logging.debug('lots of detail')
logging.info('some info')
logging.warning('a warning')
logging.error('an error')

logging.basicConfig(level=logging.DEBUG)

logging.debug('lots of detail 2')
logging.info('some info 2')
