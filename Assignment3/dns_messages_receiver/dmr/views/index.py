import flask

INDEX_BP = flask.Blueprint('index', __name__)

@INDEX_BP.route('/', methods=['GET'])
def index():

    return flask.render_template('index.html')
