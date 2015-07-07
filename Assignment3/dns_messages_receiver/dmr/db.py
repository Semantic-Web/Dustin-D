import logging

import rethinkdb

import dmr.config.log
import dmr.config.db

_LOGGER = logging.getLogger(__name__)

_CONNECTION = None
def get_connection():
    global _CONNECTION
    if _CONNECTION is None:
        _CONNECTION = \
            rethinkdb.connect(
                host=dmr.config.db.HOSTNAME, 
                port=dmr.config.db.PORT)

    return _CONNECTION

def provision_db():
    c = get_connection()

    database_name = dmr.config.db.DATABASE

    databases = rethinkdb.db_list().run(c)

    if database_name not in databases:
        _LOGGER.info("Creating DB: [{0}]".format(database_name))
        rethinkdb.db_create(database_name).run(c)
