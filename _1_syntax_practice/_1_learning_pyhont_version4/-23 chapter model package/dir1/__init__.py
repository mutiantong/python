import os

# Ensure compatibility issues are covered with pythondsn
os.environ['EVENTLET_NO_GREENDNS'] = 'yes'

# Make sure eventlet is loaded
import eventlet  # noqa
print('dir1 init')