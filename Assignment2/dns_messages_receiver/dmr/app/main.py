import flask

import dmr.config
import dmr.config.log

import dmr.views.test

app = flask.Flask(__name__)
app.debug = dmr.config.IS_DEBUG

app.register_blueprint(dmr.views.test.TEST_BP)
