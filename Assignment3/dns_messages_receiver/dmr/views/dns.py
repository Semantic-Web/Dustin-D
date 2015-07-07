import bz2
import json

import flask

DNS_BP = flask.Blueprint('dns', __name__, url_prefix='/dns')

@DNS_BP.route('/message', methods=['POST'])
def dns_message():
    data_bz2 = flask.request.get_data()
    data_encoded = bz2.decompress(data_bz2)
    message_list = json.loads(data_encoded)

    for message in message_list:
        pass

    result = {
        'count': len(message_list),
    }

    raw_response = flask.jsonify(result)
    response = flask.make_response(raw_response)

    return (response, 200)
