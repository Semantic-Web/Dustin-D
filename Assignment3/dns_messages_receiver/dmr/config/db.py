import os

HOSTNAME = os.environ.get('DMR_DB_HOSTNAME', 'localhost')
PORT = int(os.environ.get('DMR_DB_PORT', '28015'))
DATABASE = os.environ.get('DMR_DB_DATABASE_NAME', 'dmr')
