import flask
import time

TEST_BP = flask.Blueprint('test', __name__, url_prefix='/test')

@TEST_BP.route('/ping', methods=['GET'])
def test_ping():

    epoch = time.time()
    response = flask.make_response(str(epoch))

    return (response, 200)
