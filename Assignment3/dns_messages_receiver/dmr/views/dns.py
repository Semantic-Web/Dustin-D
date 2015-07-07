import bz2
import json
import datetime

import flask

import dmr.config
import dmr.config.dns
import dmr.models.dns_messages

DNS_BP = flask.Blueprint('dns', __name__, url_prefix='/dns')

@DNS_BP.route('/message', methods=['POST'])
def dns_message():
    data_bz2 = flask.request.get_data()
    data_encoded = bz2.decompress(data_bz2)
    message_list = json.loads(data_encoded)

    dm = dmr.models.dns_messages.DnsMessagesModel()

    for message in message_list:
        timestamp_dt = \
            datetime.datetime.strptime(
                message['timestamp'], 
                dmr.config.DATETIME_FORMAT)

        message['timestamp'] = \
            timestamp_dt.replace(tzinfo=dmr.config.dns.MESSAGE_TZ)

    dm.add_messages(message_list)

    result = {
        'count': len(message_list),
    }

    raw_response = flask.jsonify(result)
    response = flask.make_response(raw_response)

    return (response, 200)

@DNS_BP.route('/ajax/activity/minute', methods=['GET'])
def dns_ajax_activity_by_minute():
    now_dt = datetime.datetime.now()
    delta_td = datetime.timedelta(seconds=dmr.config.dns.ACTIVITY_CUTOFF_S)

    cutoff_dt = now_dt - delta_td

    dm = dmr.models.dns_messages.DnsMessagesModel()
    rows = dm.get_daily_activity_by_minute(cutoff_dt)
    rows = list(rows)

    result = {
        'rows': rows,
    }

    raw_response = flask.jsonify(result)
    response = flask.make_response(raw_response)

    return (response, 200)

@DNS_BP.route('/ajax/activity/hour', methods=['GET'])
def dns_ajax_activity_by_hour():
    now_dt = datetime.datetime.now()
    delta_td = datetime.timedelta(seconds=dmr.config.dns.ACTIVITY_CUTOFF_S)

    cutoff_dt = now_dt - delta_td

    dm = dmr.models.dns_messages.DnsMessagesModel()
    rows = dm.get_daily_activity_by_hour(cutoff_dt)
    rows = list(rows)

    result = {
        'rows': rows,
    }

    raw_response = flask.jsonify(result)
    response = flask.make_response(raw_response)

    return (response, 200)
