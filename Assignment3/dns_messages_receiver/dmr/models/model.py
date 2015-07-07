import logging
import contextlib
import collections

import rethinkdb

import dmr.config.db
import dmr.db

DDL_RESULT = collections.namedtuple(
                'DDL_RESULT', [
                    'unchanged',
                    'skipped',
                    'replaced',
                    'inserted',
                    'generated_keys',
                    'errors',
                    'deleted',
                ])

_LOGGER = logging.getLogger(__name__)


class Model(object):
    tables = []
    simple_indices = {}
    compound_indices = {}

    def __init__(self):
        self.__c = dmr.db.get_connection()

    def get_db(self):
        return rethinkdb.db(dmr.config.db.DATABASE)

    def get_table(self, table_name):
        return self.get_db().table(table_name)

    def __get_tables(self):
        return self.get_db().table_list().run(self.__c)

    def __get_indices(self, table_name):
        return self.get_table(table_name).index_list().run(self.__c)

    def __create_simple_index(self, table_name, field_name):
        t = self.get_table(table_name)
        
        return t.index_create(field_name).run(self.__c)

    def __create_compound_index(self, table_name, index_name, field_names):
        t = self.get_table(table_name)
        
        field_spec = \
            [[rethinkdb.row[field], rethinkdb.row[field]] 
             for field 
             in field_names]

        return t.index_create(index_name, field_spec).run(self.__c)

    def provision_tables(self):
        _LOGGER.info("Checking tables.")

        existing_tables = self.__get_tables()
        for table_name in self.__class__.tables:
            if table_name not in existing_tables:
                _LOGGER.info("Creating table: [{0}]".format(table_name))
                self.get_db().table_create(table_name).run(self.__c)

            _LOGGER.info("Checking indices for [{0}].".format(table_name))

            existing_indices = self.__get_indices(table_name)

            simple_indices = \
                self.__class__.simple_indices.get(table_name, [])

            for field_name in simple_indices:
                if field_name not in existing_indices:
                    _LOGGER.info("Creating simple index: [{0}]-[{1}]".\
                                 format(table_name, field_name))

                    self.__create_simple_index(table_name, field_name)

            compound_indices = \
                self.__class__.compound_indices.get(table_name, [])

            for index_name, field_names in compound_indices:
                if index_name not in existing_indices:
                    _LOGGER.info("Creating compound index: [{0}]-[{1}]: {2}".\
                                 format(table_name, index_name, field_names))

                    self.__create_compound_index(table_name, index_name, field_names)

    def insert_record(self, table_name, **kwargs):
        raw = self.get_table(table_name).insert([kwargs]).run(self.__c)
        r = DDL_RESULT(**raw)

        return r.generated_keys[0]

    def insert_records(self, table_name, rows):
        raw = self.get_table(table_name).insert(rows).run(self.__c)
        return DDL_RESULT(**raw)

    @property
    def connection(self):
        return dmr.db.get_connection()
