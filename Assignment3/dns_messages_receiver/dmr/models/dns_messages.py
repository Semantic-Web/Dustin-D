import datetime

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

    def add_message(self, timestamp, type_, hostname, conjunction, ip):
        assert issubclass(timestamp.__class__, datetime.datetime), \
               "Timestamp must be a datetime."

        id_ = self.insert_record(
                _TABLE_DNS_MESSAGES,
                timestamp=timestamp,
                type=type_,
                hostname=hostname,
                conjunction=conjunction,
                ip=ip)

        return id_

    def get_daily_activity(self):
        t = self.get_table(_TABLE_DNS_MESSAGES)
        g = t.group('timestamp', 'type')
        return g.count()
