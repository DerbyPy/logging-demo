from __future__ import print_function

import logging

root = logging.getLogger()
usa = logging.getLogger('usa')
ky = logging.getLogger('usa.ky')
louisville = logging.getLogger('usa.ky.louisville')

root.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
root.addHandler(stream_handler)
root.addHandler(logging.FileHandler('root.log'))
usa.addHandler(logging.FileHandler('usa.log'))
ky.addHandler(logging.FileHandler('ky.log'))
louisville.addHandler(logging.FileHandler('louisville.log'))


root.info('root')
usa.info('usa')
ky.info('ky')
louisville.info('louisville')

print('# Warning level')
stream_handler.setLevel(logging.WARNING)
ky.info('ky 2')
louisville.warning('louisville 2')
