from __future__ import print_function

import logging

import sqlalchemy

logging.basicConfig()

print('# No logger')
engine = sqlalchemy.create_engine('sqlite:///')
engine.execute('select sqlite_version()')


print('# Engine logger')
engine_logger = logging.getLogger('sqlalchemy.engine')
engine_logger.setLevel(logging.INFO)

engine = sqlalchemy.create_engine('sqlite:///')
engine.execute('select sqlite_version()')

print('# Pool logger')
pool_logger = logging.getLogger('sqlalchemy.pool')
pool_logger.setLevel(logging.DEBUG)

engine.execute('select sqlite_version()')

