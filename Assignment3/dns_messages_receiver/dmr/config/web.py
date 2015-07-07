import os.path

_RESOURCES_PATH = \
    os.path.abspath(os.path.join(
        os.path.dirname(__file__), 
        '..', 
        'resources'))

TEMPLATE_PATH = os.path.join(_RESOURCES_PATH, 'templates')
STATIC_PATH = os.path.join(_RESOURCES_PATH, 'static')
