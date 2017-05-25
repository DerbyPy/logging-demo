from __future__ import print_function

import logging

import sqlalchemy

logging.basicConfig()

print('# Root logger')
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

# No logs
engine = sqlalchemy.create_engine('sqlite:///')
engine.execute('select sqlite_version()')

print('# Engine debug')
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)
engine.execute('select sqlite_version()')

print('# Engine debug, root override')
root_logger.setLevel(logging.ERROR)
engine.execute('select sqlite_version()')
