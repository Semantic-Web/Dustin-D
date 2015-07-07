import datetime

import rethinkdb

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
        t = self.get_table(_TABLE_DNS_MESSAGES)
        
        cutoff_phrase = cutoff_dt.strftime(dmr.config.DATETIME_FORMAT)

        rows = t.filter(rethinkdb.row['timestamp'].lt(cutoff_phrase))\
                .group([
                    rethinkdb.row['timestamp'].year(), 
                    rethinkdb.row['timestamp'].month(), 
                    rethinkdb.row['timestamp'].day(), 
                    rethinkdb.row['timestamp'].hours(), 
                    rethinkdb.row['timestamp'].minutes(), 
                    rethinkdb.row['type']])\
                .count()\
                .run(self.connection)

        for group, count in rows.items():
            (year, month, day, hour, minute, type_) = group
            yield ((year, month, day, hour, minute), type_, count)

    def get_daily_activity_by_hour(self, cutoff_dt):
        t = self.get_table(_TABLE_DNS_MESSAGES)
        
        cutoff_phrase = cutoff_dt.strftime(dmr.config.DATETIME_FORMAT)

        rows = t.filter(rethinkdb.row['timestamp'].lt(cutoff_phrase))\
                .group([
                    rethinkdb.row['timestamp'].year(), 
                    rethinkdb.row['timestamp'].month(), 
                    rethinkdb.row['timestamp'].day(), 
                    rethinkdb.row['timestamp'].hours(), 
                    rethinkdb.row['type']])\
                .count()\
                .run(self.connection)

        for group, count in rows.items():
            (year, month, day, hour, type_) = group
            yield ((year, month, day, hour), type_, count)
