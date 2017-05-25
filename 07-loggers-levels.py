from __future__ import print_function

import logging

root = logging.getLogger()
usa = logging.getLogger('usa')
ky = logging.getLogger('usa.ky')
louisville = logging.getLogger('usa.ky.louisville')

print('NOTSET: {0.NOTSET}, DEBUG: {0.DEBUG}, INFO: {0.INFO}, WARNING: {0.WARNING}'.format(logging))


def print_levels(label):
    print(label)
    print('  root', root.level)
    print('  usa', usa.level, usa.getEffectiveLevel())
    print('  ky', ky.level, ky.getEffectiveLevel())
    print('  louisville', louisville.level, louisville.getEffectiveLevel())
    raw_input('continue? ')


print_levels('# Default')

usa.setLevel(logging.DEBUG)
print_levels('# Set USA')

ky.setLevel(logging.INFO)
print_levels('# Set KY')

louisville.setLevel(logging.WARNING)
print_levels('# Set louisville')
