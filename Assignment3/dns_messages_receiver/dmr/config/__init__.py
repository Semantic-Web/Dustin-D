import os

IS_DEBUG = bool(int(os.environ.get('DEBUG', '0')))
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
