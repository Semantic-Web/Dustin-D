import flask

import dmr.config
import dmr.config.web
import dmr.config.log

import dmr.views.index
import dmr.views.dns
import dmr.views.test

app = flask.Flask(__name__, template_folder=dmr.config.web.TEMPLATE_PATH)
app.debug = dmr.config.IS_DEBUG

app.register_blueprint(dmr.views.dns.DNS_BP)
app.register_blueprint(dmr.views.test.TEST_BP)
app.register_blueprint(dmr.views.index.INDEX_BP)
