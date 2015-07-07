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

    def add_messages(self, rows):
        self.insert_records(_TABLE_DNS_MESSAGES, rows)

    def get_daily_activity(self):
        t = self.get_table(_TABLE_DNS_MESSAGES)
        g = t.group('timestamp', 'type')
        return g.count()
