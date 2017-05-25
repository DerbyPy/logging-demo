from __future__ import print_function

import logging


def logger_info(*loggers):
    print('# Logger info:')
    for logger in loggers:
        parent_name = logger.parent.name if logger.parent else None
        print('    ', logger.name, ' -> ', parent_name)


logging.basicConfig(level=logging.INFO)

root = logging.getLogger()

auto = logging.getLogger('auto')
toyota = logging.getLogger('auto.toyota')
honda = logging.getLogger('auto.honda')

company = logging.getLogger('company')
google = logging.getLogger('company.google')
amazon = logging.getLogger('company.amazon')


louisville = logging.getLogger('usa.ky.louisville')
ky = logging.getLogger('usa.ky')

logger_info(root, auto, toyota, honda, company, google, amazon, louisville)

# print('# Logs:')
# auto.info('cars')
# louisville.info('python!')

louisville.propagate = False

louisville.info('fail')

# Add a handler directly on the louisville logger
handler = logging.StreamHandler()
louisville.addHandler(handler)

louisville.info('success')

# Now our direct handler and the root handler will log the message.
louisville.propagate = True
louisville.info('2x success')

