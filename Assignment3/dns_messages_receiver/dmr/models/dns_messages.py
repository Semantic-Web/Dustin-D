import datetime

import rethinkdb
import pytz

import dmr.config
import dmr.models.model

_TABLE_DNS_MESSAGES = 'dns_messages'


class DnsMessagesModel(dmr.models.model.Model):
    tables = [
        _TABLE_DNS_MESSAGES,
    ]

    compound_indices = {
        _TABLE_DNS_MESSAGES: [
            ('dns_messages_idx', ['timestamp', 'type']),
        ],
    }

    def add_messages(self, rows):
        self.insert_records(_TABLE_DNS_MESSAGES, rows)

    def get_daily_activity_by_minute(self, cutoff_dt):
        assert cutoff_dt.tzinfo is not None, \
               "Cutoff timestamp must be timezone-aware."

        cutoff_dt = cutoff_dt.astimezone(pytz.UTC)

        t = self.get_table(_TABLE_DNS_MESSAGES)
        
        rows = t.filter(
                    rethinkdb.row['timestamp'].during(
                        rethinkdb.time(
                            cutoff_dt.year, 
                            cutoff_dt.month, 
                            cutoff_dt.day, 
                            cutoff_dt.hour, 
                            cutoff_dt.minute, 
                            cutoff_dt.second,
                            'Z'
                        ), 
                        rethinkdb.now()
                    )
                )\
                .filter(
                    lambda row: row['type'].match('^query')
                )\
                .group([
                    rethinkdb.row['timestamp'].year(), 
                    rethinkdb.row['timestamp'].month(), 
                    rethinkdb.row['timestamp'].day(), 
                    rethinkdb.row['timestamp'].hours(), 
                    rethinkdb.row['timestamp'].minutes(), 
                    rethinkdb.row['type']
                ])\
                .count()\
                .run(self.connection)

        for group, count in rows.items():
            (year, month, day, hour, minute, type_) = group
            yield ((year, month, day, hour, minute), type_, count)

    def get_daily_activity_by_hour(self, cutoff_dt):
        assert cutoff_dt.tzinfo is not None, \
               "Cutoff msut be timezone-aware."

        cutoff_dt = cutoff_dt.astimezone(pytz.UTC)

        t = self.get_table(_TABLE_DNS_MESSAGES)
        
        rows = t.filter(
                    rethinkdb.row['timestamp'].during(
                        rethinkdb.time(
                            cutoff_dt.year, 
                            cutoff_dt.month, 
                            cutoff_dt.day, 
                            cutoff_dt.hour, 
                            cutoff_dt.minute, 
                            cutoff_dt.second,
                            'Z'
                        ), 
                        rethinkdb.now()
                    )
                )\
                .filter(
                    lambda row: row['type'].match('^query')
                )\
                .group([
                    rethinkdb.row['timestamp'].year(), 
                    rethinkdb.row['timestamp'].month(), 
                    rethinkdb.row['timestamp'].day(), 
                    rethinkdb.row['timestamp'].hours(), 
                    rethinkdb.row['type']]
                )\
                .count()\
                .run(self.connection)

        for group, count in rows.items():
            (year, month, day, hour, type_) = group
            yield ((year, month, day, hour), type_, count)

